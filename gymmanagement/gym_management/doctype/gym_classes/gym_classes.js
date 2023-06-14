// Copyright (c) 2023, Mr Ameen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Classes', {
	// refresh: function(frm) {

	// }
	refresh: function(frm) {
		
		cur_frm.fields_dict['trainer_user'].get_query = function(doc) {
			return {
				filters: {
					"type_trainer": 'Class'
				}
			}
		};
		
	},
});
