from flask_restx import Namespace, Resource, reqparse

from main.service.common import get_network_request_payloads

response_namespace = Namespace('response', description='Response Namespace')


@response_namespace.route("/v1/response/network-request-payloads")
class GetNetworkRequestPayloads(Resource):

    def create_parser_with_args(self):
        parser = reqparse.RequestParser()
        parser.add_argument("select", dest='retail_select', required=False)
        parser.add_argument("init", dest="retail_init", required=False)
        parser.add_argument("confirm", dest="retail_confirm", required=False)
        parser.add_argument("status", dest="retail_status", required=False)
        parser.add_argument("track", dest="retail_track", required=False)
        parser.add_argument("support", dest="retail_support", required=False)
        parser.add_argument("cancel", dest="retail_cancel", required=False)
        parser.add_argument("update", dest="retail_update", required=False)
        parser.add_argument("issue", dest="retail_issue", required=False)
        parser.add_argument("issue_status", dest="retail_issue_status", required=False)
        return parser.parse_args()

    def get(self):
        args = self.create_parser_with_args()
        return get_network_request_payloads(**args)

