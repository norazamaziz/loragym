// Copyright (c) 2023, Mr Ameen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {
	// refresh: function(frm) {

	// }
	refresh: function(frm) {
		frm.fields_dict['pick_locker'].grid.get_field('service_locker').get_query = function(){
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
	var pick_locker = frm2.doc.pick_locker;
	var arrcurrent_pick_locker = [];
	for(var i=0;i<pick_locker.length;i++)
	{
		var tr = pick_locker[i].service_locker;
		if (tr!=undefined) arrcurrent_pick_locker.push(tr);
	}
	console.log(arrcurrent_pick_locker)
	return arrcurrent_pick_locker;
}

frappe.ui.form.on('Gym Locker Child',"name",function(frm,cdt,cdn){
	let selectedRow = locals[cdt][cdn];
	frm.refresh_field('service_locker');
	console.log('selectedRow');
	console.log(selectedRow);
})