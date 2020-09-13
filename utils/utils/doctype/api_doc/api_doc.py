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

	def get_api_success(self):
		success = ""
		for success_ in self.success:
			s = ["@apiSuccess"]
			
			if success_.group:
				s.append("({})".format(success_.group))
			
			s.append("{{{}}}".format(success_.type))

			field = success_.field
			if success_.default_value:
				field += "=\"{}\"".format(success_.default_value)
			s.append(field)

			if success_.description:
				s.append(success_.description)

			success += "{}\n".format(' '.join(s))

		return success

	def get_api_success_example(self):
		success_example = ""
		for success_example_ in self.success_example:
			se = ["@apiSuccessExample"]

			se.append(success_example_.title)

			success_example += "{}\n{}\n".format(' '.join(se), success_example_.example)

		return success_example

	def get_api_error(self):
		error = ""
		for error_ in self.error:
			e = ["@apiError"]
			
			if error_.group:
				e.append("({})".format(error_.group))
			
			e.append("{{{}}}".format(error_.type))

			field = error_.field
			if error_.default_value:
				field += "=\"{}\"".format(error_.default_value)
			e.append(field)

			if error_.description:
				e.append(error_.description)

			error += "{}\n".format(' '.join(e))

		return error

	def get_api_error_example(self):
		error_example = ""
		for error_example_ in self.error_example:
			ee = ["@apiErrorExample"]

			ee.append(error_example_.title)

			error_example += "{}\n{}\n".format(' '.join(ee), error_example_.example)

		return error_example


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
		block += self.get_api_success()
		block += self.get_api_success_example()
		block += self.get_api_error()
		block += self.get_api_error_example()
		block += "\"\"\"\n\n"

		return block


@frappe.whitelist()
def generate_api_docs(app_name):
	import os
	from json import dumps

	apidocs_main_folder = frappe.get_app_path(app_name, '..', '..', '..', 'config', 'apidocs')
	apidocs_output_folder = frappe.get_app_path(app_name, 'public', 'apidocs')

	# create directories
	os.mkdir(apidocs_main_folder)

	# writing apidoc blocks
	f = open(os.path.join(apidocs_main_folder, 'apidoc.py'), 'a+')
	for apidoc_name in [a[0] for a in frappe.db.sql('select name from `tabAPI Doc`')]:
		apidoc = frappe.get_doc('API Doc', apidoc_name)
		f.write(apidoc.generate_apidoc_comment())
	f.close()

	# writing apidoc.json
	app = __import__(app_name)
	apidoc_json = {
		'name': "{} API Docs".format(frappe.get_site_path().replace('./', '').title()),
		'version': app.__version__
	}
	f = open(os.path.join(apidocs_main_folder, 'apidoc.json'), 'a+')
	f.write(dumps(apidoc_json))
	f.close()

	# generating apidoc output
	cmd = "{app_location}/../node_modules/.bin/apidoc -i {src} -o {output} -c {config}".format(
		app_location=frappe.get_app_path('utils'), 
		src=apidocs_main_folder, 
		output=apidocs_output_folder,
		config=os.path.join(apidocs_main_folder, 'apidoc.json')
	)
	utils.system_command(cmd)

	# deleting apidocs_main_folder
	from shutil import rmtree
	rmtree(apidocs_main_folder)

	


