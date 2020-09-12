# -*- coding: utf-8 -*-
# Copyright (c) 2020, Neel Bhanushali and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import utils

class APIDoc(Document):
	def before_save(self):
		# non grouped entries to be grouped under Miscellaneous
		# except for @apiDefine
		if not self.group and not self.api_define:
			self.group = "Miscellaneous"

		# @apiDefine title will be without spaces
		if self.api_define:
			self.title = self.title.replace(' ', '')

		# set api_doc_title for @apiUse multiselect
		for api in self.use_api_define:
			api.api_doc_title = frappe.db.get_value('API Doc', api.api_doc, 'title')
	
	def get_api(self):
		if not self.path:
			return ""

		return "@api {{{method}}} {path} {title}\n".format(method=self.method, path=self.path, title=self.title)

	def get_api_name(self):
		if self.api_define:
			return "@apiDefine {title}\n".format(title=self.title)
		else:
			return "@apiName {name}\n".format(name=self.title)

	def get_api_group(self):
		if not self.group:
			return ""
		return "@apiGroup {group}\n".format(group=self.group)

	def get_api_version(self):
		output = ""
		if self.version:
			output = "@apiVersion {version}\n".format(version=self.version)
		return output

	def get_api_headers(self):
		headers = ""
		for header in self.headers:
			h = ["@apiHeader"]
			
			if header.group:
				h.append("({})".format(header.group))
			
			h.append("{{{}}}".format(header.type))

			field = header.field
			if header.default_value:
				field += "=\"{}\"".format(header.default_value)
			if header.optional:
				field = "[{}]".format(field)
			h.append(field)

			if header.description:
				h.append(header.description)

			headers += "{}\n".format(' '.join(h))

		return headers

	def get_api_headers_example(self):
		headers_example = ""
		for header_example in self.headers_example:
			he = ["@apiHeaderExample"]

			he.append(header_example.title)

			headers_example += "{}\n{}\n".format(' '.join(he), header_example.example)

		return headers_example

	def get_api_parameters(self):
		parameters = ""
		for parameter in self.parameters:
			p = ["@apiParam"]
			
			if parameter.group:
				p.append("({})".format(parameter.group))
			
			type_ = parameter.type
			if parameter.size:
				type_ += "{{{}}}".format(parameter.size)
			if parameter.allowed_values:
				type_ += "=\"{}\"".format(parameter.allowed_values)
			p.append("{{{}}}".format(type_))

			field = parameter.field
			if parameter.default_value:
				field += "=\"{}\"".format(parameter.default_value)
			if parameter.optional:
				field = "[{}]".format(field)
			p.append(field)

			if parameter.description:
				p.append(parameter.description)

			parameters += "{}\n".format(' '.join(p))

		return parameters

	def get_api_parameters_example(self):
		parameters_example = ""
		for parameter_example in self.parameters_example:
			he = ["@apiParamExample"]

			he.append(parameter_example.title)

			parameters_example += "{}\n{}\n".format(' '.join(he), parameter_example.example)

		return parameters_example

	def get_api_uses(self):
		api_uses = ""
		for api_use in self.use_api_define:
			api_uses += "@apiUse {}\n".format(api_use.api_doc_title)

		return api_uses


	def generate_apidoc_comment(self):
		block = "\"\"\"\n"
		block += self.get_api()
		block += self.get_api_name()
		block += self.get_api_group()
		block += self.get_api_version()
		block += self.get_api_headers()
		block += self.get_api_headers_example()
		block += self.get_api_parameters()
		block += self.get_api_parameters_example()
		block += self.get_api_uses()
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

	


