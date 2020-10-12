from frappe import _
from .APIException import APIException

class MethodNotAllowedException(APIException):
	http_status_code = 405
	message = _('Method not allowed')
	save_error_log = False