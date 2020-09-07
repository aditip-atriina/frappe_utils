import frappe
import json
from werkzeug.wrappers import Response

class Responder:
    def respond(self, status=200, message='Success', data={}, errors={}):
        response = frappe._dict({'message': message})
        if data:
            response['data'] = data
        if errors:
            response['errors'] = errors

        return Response(response=json.dumps(response), status=status, content_type='application/json')