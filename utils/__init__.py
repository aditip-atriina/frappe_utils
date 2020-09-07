# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

import frappe
from utils.responder import Responder
responder = Responder()

# class JsonException(Exception):
# 	"""
# 	Exception that returns JSON Response
# 	Extend all Application Exceptions 
# 	from this class to want a JSON Response
# 	"""
# 	headers = dict(frappe.request.headers)
# 	headers['Accept'] = 'application/json'
# 	frappe.request.headers = headers

# def validate_input(data=None, rules=None):
# 	raise ValidationException({'asd': 'jkslkasd', 'jkdjk': 'lkjasdjlasf'})

# class ValidationException(JsonException):
# 	http_status_code = 422

# 	def __init__(self, errors):
# 		respond(message='Validation Exception', errors=errors)

# def respond(http_status_code=200, message='Success', data={}, errors={}):
# 	frappe.response.http_status_code = http_status_code
# 	frappe.response.message = message
# 	if data:
# 		frappe.response.data = data
# 	if errors:
# 		frappe.response.errors = errors