# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '1.0.2'

import frappe

from .responder import *
from .exceptions import *
from .validator import *
from .tests import *

def system_command(cmd):
	import subprocess
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	return process.communicate()

def create_user_access_token(user_name):
	from frappe.core.doctype.user.user import generate_keys
	res = generate_keys(user_name)
	frappe.db.commit()
	api_key = frappe.db.get_value('User', user_name, 'api_key')
	api_secret = res['api_secret']

	return 'token {}:{}'.format(api_key, api_secret)