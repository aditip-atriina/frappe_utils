import frappe
from ..responder import responder
class APIException(Exception):
	"""
	Base Exception for API Requests

	Usage:
	try:
		...
	except APIException as e:
		return e.respond()
	"""

	http_status_code = 500
	message = frappe._('Something went Wrong')
	save_error_log = True
	
	def __init__(self, message=None, errors={}):
		if message:
			self.message = message
		self.errors = errors

	def respond(self):
		if self.save_error_log:
			frappe.log_error()
		return responder.respond(status=self.http_status_code, message=self.message, errors=self.errors)