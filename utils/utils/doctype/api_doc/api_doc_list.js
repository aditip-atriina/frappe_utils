frappe.listview_settings['API Doc'] = {
	onload: function(listview) {
		listview.page.add_inner_button(__("Generate API Docs"), function() {
			frappe.prompt('Enter App Name', ({value}) => { 
				window.open('/api/method/utils.utils.doctype.api_doc.api_doc.generate_api_docs?app_name=' + value)
			})
		});
	}
};