// Copyright (c) 2023, Mr Ameen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership', {
	// refresh: function(frm) {

	// }
	refresh: function(frm) {
		frm.fields_dict['pick_locker_membership'].grid.get_field('service_locker').get_query = function(){
			var data = {
				filters:[
					['Gym Locker','status','=','Availaible'],
					['Gym Locker','name1','not in',getExisted(frm)]
				]
			};
			// console.log('data')
			// console.log(data);
			return data
		};


        frm.set_value(
            "remaining_days_left",
            frappe.datetime.get_day_diff(frm.doc.end_plan,frm.doc.start_plan)
        );
		cur_frm.save();

	},
	// after_save: function(frm) {
	// 	frappe.call({
	// 		method:'service_station.services.rest.create_sales_invoice',
	// 		args: {
	// 			'inspection': frm.doc.name
	// 		},
	// 		callback: function(r) {
	// 			//
	// 		}
	// 	});
	// 	// frappe.validated = false; // it will not be submitted for testing
		
	// }
});

function getExisted(frm2)
{
	console.log('getExisted()');
	console.log(frm2);
	var pick_locker_membership = frm2.doc.pick_locker_membership;
	var arrcurrent_pick_locker = [];
	for(var i=0;i<pick_locker_membership.length;i++)
	{
		var tr = pick_locker_membership[i].service_locker;
		if (tr!=undefined) arrcurrent_pick_locker.push(tr);
	}
	console.log(arrcurrent_pick_locker)
	return arrcurrent_pick_locker;
}