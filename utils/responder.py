import frappe
import json
from werkzeug.wrappers import Response

class Responder:
    def respond(self, status=200, message='Success', data={}, errors={}):
        response = frappe._dict({'message': frappe._(message)})
        if data:
            response['data'] = data
        if errors:
            response['errors'] = errors

        return Response(response=json.dumps(response), status=status, content_type='application/json')

    def respondWithSuccess(self, status=200, message='Success', data={}):
        return self.respond(status=status, message=message, data=data)

    def respondWithFailure(self, status=500, message='Something went wrong', data={}, errors={}):
        return self.respond(status=status, message=message, data=data, errors=errors)

    def respondUnauthorized(self, status=401, message='Unauthorized'):
        return self.respond(status=status, message=message)

    def respondForbidden(self, status=403, message='Forbidden'):
        return self.respond(status=status, message=message)