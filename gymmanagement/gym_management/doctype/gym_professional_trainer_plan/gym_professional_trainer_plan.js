// Copyright (c) 2023, Mr Ameen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Professional Trainer Plan', {
	refresh: function(frm) {
		cur_frm.fields_dict['plan_name'].get_query = function(doc) {
			return {
				filters: {
					"plan_type": 'Professional'
				}
			}
		}
	}
});
