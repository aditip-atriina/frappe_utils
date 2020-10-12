import unittest

class APITestCase(unittest.TestCase):
	def assertSuccess(self, res):
		self.assertEqual(res.status_code, 200)

	def assertNotFound(self, res):
		self.assertEqual(res.status_code, 404)

	def assertUnauthorized(self, res):
		self.assertEqual(res.status_code, 401)

	def assertForbidden(self, res):
		self.assertEqual(res.status_code, 403)

	def assertNotFound(self, res):
		self.assertEqual(res.status_code, 404)

	def assertValidationError(self, res):
		self.assertEqual(res.status_code, 422)

	def assertFailure(self, res):
		self.assertEqual(res.status_code, 500)
