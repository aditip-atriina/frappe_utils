# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'

import frappe
from utils.responder import Responder
responder = Responder()

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
