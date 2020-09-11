frappe.listview_settings['API Doc'] = {
	onload: function(listview) {
		listview.page.add_inner_button(__("Generate API Docs"), function() {
			frappe.call({
                method: 'utils.utils.doctype.api_doc.api_doc.generate_api_docs',
                freeze: true,
            })
		});
	}
};