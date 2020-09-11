from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
        {
			"label": _("API Documentation"),
			"icon": "fa fa-glass",
			"items": [
				{
					"type": "doctype",
					"name": "API Doc",
				}
			]
		}
	]
