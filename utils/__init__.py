# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '1.0.2'

import frappe

from utils.responder import *
# from utils.exceptions import *
# from utils.exceptions import APIException, MethodNotAllowedException, ValidationException
from utils.validator import *
from utils.tests import *

def system_command(cmd):
	import subprocess
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	return process.communicate()

def create_user_access_token(user_name):
	user_details = frappe.get_doc('User', user_name)
	api_secret = frappe.generate_hash(length=15)
	# if api key is not set generate api key
	if not user_details.api_key:
		api_key = frappe.generate_hash(length=15)
		user_details.api_key = api_key
	user_details.api_secret = api_secret
	user_details.save(ignore_permissions=True)

	return 'token {}:{}'.format(user_details.api_key, api_secret)

def frappe_doc_proper_dict(doc):
	doc = doc.as_json()
	from json import loads
	return loads(doc)
