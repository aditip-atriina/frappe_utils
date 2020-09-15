import frappe
import unittest
from utils.api import test

class APITest(unittest.TestCase):
	def test_validation_error(self):
		res = test(email="", first_name=None, last_name=None)
		self.assertEqual(res.status_code, 422)

	def test_success(self):
		res = test(email="asdf@asdf.com", first_name="john", last_name="doe")
		self.assertEqual(res.status_code, 200)