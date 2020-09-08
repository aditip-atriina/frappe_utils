# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

import frappe
from utils.responder import Responder
responder = Responder()

from validator import validate as validate_

def validate(data, rules):
	valid, valid_data, errors = validate_(data, rules, return_info=True)

	if not valid:
		raise ValidationException(errors=errors)

	return valid_data

class APIException(Exception):
	"""
	Base Exception for API Requests

	Usage:
	try:
		...
	except APIException as e:
		return e.respond()
	"""

	http_status_code = message = None
	
	def __init__(self, message=frappe._('Something went Wrong'), errors={}):
		if not self.message:
			self.message = message
		self.errors = errors

	def respond(self):
		return responder.respond(status=self.http_status_code, message=self.message, errors=self.errors)

class ValidationException(APIException):
	http_status_code = 422
	message = frappe._('Validation Error')

	def __init__(self, errors):
		errors_ = dict()
		for key in errors.keys():
			# getting first error message
			errors_[key] = list(errors[key].values())[0]
		self.errors = errors_
