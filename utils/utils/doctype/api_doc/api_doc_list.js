frappe.listview_settings['API Doc'] = {
	onload: function(listview) {
		listview.page.add_inner_button(__("Generate API Docs"), function() {
			frappe.prompt('Enter App Name', ({value}) => { 
				frappe.call({
					method: 'utils.utils.doctype.api_doc.api_doc.generate_api_docs',
					freeze: true,
					freeze_message: 'Generating API Docs. Please wait...',
					args: {
						app_name: value
					}
				})
			})
		});
	}
};