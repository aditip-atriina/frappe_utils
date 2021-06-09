from .rules import *
# from utils.exceptions import ValidationException, MethodNotAllowedException

from validator import validate as validate_
def validate(data, rules):
	valid, valid_data, errors = validate_(data, rules, return_info=True)

	if not valid:
		from utils.exceptions import ValidationException
		raise ValidationException(errors=errors)

	return valid_data

def validate_http_method(*methods):
	if frappe.request:
		if frappe.request.method.upper() not in [method.upper() for method in methods]:
			from utils.exceptions import MethodNotAllowedException
			raise MethodNotAllowedException
