// Copyright (c) 2020, Neel Bhanushali and contributors
// For license information, please see license.txt

frappe.ui.form.on('API Doc', {
	refresh: function(frm) {
		frm.fields_dict['use_api_define'].get_query = function() { 
			return {
				filters: {
					api_define: 1
				} 
			}
		}
	}
});
