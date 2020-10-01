from frappe import _
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

	http_status_code = message = None
	
	def __init__(self, message=_('Something went Wrong'), errors={}):
		if not self.message:
			self.message = message
		self.errors = errors

	def respond(self):
		return responder.respond(status=self.http_status_code, message=self.message, errors=self.errors)