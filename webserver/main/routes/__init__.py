import os

from flask_restx import Api as BaseAPI
from jsonschema import ValidationError
from werkzeug.exceptions import BadRequest

from main.models.error import BaseError
from main.repository.ack_response import get_ack_response
from main.routes.retail.cancel import cancel_namespace
from main.routes.retail.cancellation_reasons import cancellation_reasons_namespace
from main.routes.retail.confirm import confirm_namespace
from main.routes.retail.init import init_namespace
from main.routes.retail.rating import rating_namespace
from main.routes.response import response_namespace
from main.routes.retail.search import search_namespace
from main.routes.retail.select import select_namespace
from main.routes.retail.status import status_namespace
from main.routes.retail.support import support_namespace
from main.routes.retail.track import track_namespace
from main.routes.retail.update import update_namespace
from main.utils.schema_utils import transform_json_schema_error
from main.routes.retail.issue import issue_namespace
from main.routes.retail.issue_status import issue_status_namespace


class Api(BaseAPI):
    def _register_doc(self, app_or_blueprint):
        # HINT: This is just a copy of the original implementation with the last line commented out.
        if self._add_specs and self._doc:
            # Register documentation before root if enabled
            app_or_blueprint.add_url_rule(self._doc, 'doc', self.render_doc)

    @property
    def base_path(self):
        return ''


api = Api(
    title='ONDC API',
    version='1.0',
    description='Rest api for ONDC dashboard project',
    doc='/swagger/' if os.getenv("ENV") != None else False
)



@api.errorhandler(BadRequest)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        error_message = transform_json_schema_error(error.description)
        return get_ack_response(ack=False,
                                error={"type": BaseError.JSON_SCHEMA_ERROR.value, "message": error_message}), 400
    # handle other "Bad Request"-errors
    return str(error), 500


@api.errorhandler(ValidationError)
def bad_request(error):
    return {'error': str(error), 'message': error.message}, 400


api.add_namespace(cancel_namespace, path='/protocol')
api.add_namespace(cancellation_reasons_namespace, path='/protocol')
api.add_namespace(confirm_namespace, path='/protocol')
api.add_namespace(init_namespace, path='/protocol')
api.add_namespace(rating_namespace, path='/protocol')
api.add_namespace(search_namespace, path='/protocol')
api.add_namespace(select_namespace, path='/protocol')
api.add_namespace(status_namespace, path='/protocol')
api.add_namespace(support_namespace, path='/protocol')
api.add_namespace(track_namespace, path='/protocol')
api.add_namespace(update_namespace, path='/protocol')
api.add_namespace(issue_namespace, path='/protocol')
api.add_namespace(issue_status_namespace, path='/protocol')
api.add_namespace(response_namespace, path='/protocol')
