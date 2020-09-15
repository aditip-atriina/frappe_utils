import frappe
import utils

@frappe.whitelist(allow_guest=True)
def test(*args, **kwargs):
	try:
		data = utils.validate(dict(kwargs), {
			'first_name': 'required',
			'last_name': 'required',
			'email': 'required|mail'
		})

		return utils.responder.respondWithSuccess(data=data)
	except utils.APIException as e:
		return e.respond()
