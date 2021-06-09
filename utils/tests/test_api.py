import frappe
import utils

class APITest(utils.tests.APITestCase):
	@classmethod
	def setUpClass(cls):
		cls.client = utils.FrappeClient('http://localhost:8003', user='Administrator')

	def test_validation_error(self):
		res = self.client.get_api('utils.api.test', {'email': ''})
		self.assertValidationError(res)

	def test_success(self):
		res = self.client.get_api('utils.api.test', {'email': 'asdf@asdf.com', 'first_name': 'john', 'last_name': 'doe'})
		self.assertSuccess(res)