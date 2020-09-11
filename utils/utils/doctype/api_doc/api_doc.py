# -*- coding: utf-8 -*-
# Copyright (c) 2020, Neel Bhanushali and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import utils

class APIDoc(Document):
	def get_api(self):
		return "@api {{{method}}} {path} {title}".format(method=self.method, path=self.path, title=self.title)

	def get_api_name(self):
		return "@apiName {name}".format(name=self.title)

	def get_api_group(self):
		return "@apiGroup {group}".format(group=self.group)

	def generate_apidoc_comment(self):
		block = "\"\"\"\n"
		block += self.get_api() + "\n"
		block += self.get_api_name() + "\n"
		block += self.get_api_group() + "\n"
		block += "\"\"\"\n\n"

		return block


@frappe.whitelist()
def generate_api_docs():
	import os
	from json import dumps

	apidocs_main_folder = frappe.get_app_path('utils', '..', '..', '..', 'config', 'apidocs')
	apidocs_output_folder = frappe.get_app_path('utils', 'public', 'apidocs')

	# create directories
	os.mkdir(apidocs_main_folder)

	# writing apidoc blocks
	f = open(os.path.join(apidocs_main_folder, 'apidoc.py'), 'a+')
	for apidoc_name in [a[0] for a in frappe.db.sql('select name from `tabAPI Doc`')]:
		apidoc = frappe.get_doc('API Doc', apidoc_name)
		f.write(apidoc.generate_apidoc_comment())
	f.close()

	# writing apidoc.json
	apidoc_json = {
		'name': frappe.get_site_path().replace('./', '')
	}
	f = open(os.path.join(apidocs_main_folder, 'apidoc.json'), 'a+')
	f.write(dumps(apidoc_json))
	f.close()

	# generating apidoc output
	cmd = "{app_location}/../node_modules/apidoc/bin/apidoc -i {src} -o {output} -c {config}".format(
		app_location=frappe.get_app_path('utils'), 
		src=apidocs_main_folder, 
		output=apidocs_output_folder,
		config=os.path.join(apidocs_main_folder, 'apidoc.json')
	)
	utils.system_command(cmd)

	# deleting apidocs_main_folder
	from shutil import rmtree
	rmtree(apidocs_main_folder)

	


