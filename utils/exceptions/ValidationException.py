from frappe import _
from .APIException import APIException

class ValidationException(APIException):
	http_status_code = 422
	message = _('Validation Error')

	def __init__(self, errors):
		errors_ = dict()
		for key in errors.keys():
			# getting first error message
			errors_[key] = list(errors[key].values())[0]
		self.errors = errors_