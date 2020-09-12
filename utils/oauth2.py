import frappe

def setup():
	frappe_server_url = frappe.db.get_value("Social Login Key", "frappe", "base_url") or None
	if not frappe_server_url:
		client = frappe.new_doc('OAuth Client')
		client.app_name = "Frappe"
		client.default_redirect_uri = frappe.utils.get_url('/api/method/frappe.www.login.login_via_frappe')
		client.insert()
		frappe.db.commit()

		ss = frappe.new_doc('Social Login Key')
		ss.social_login_provider = "Frappe"
		ss.client_id = client.client_id
		ss.client_secret = client.client_secret
		data = ss.get_social_login_provider(ss.social_login_provider)
		ss.update(data)
		ss.base_url = frappe.utils.get_url()
		ss.insert()
		frappe.db.commit()