// Copyright (c) 2023, Mr Ameen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Trainer', {
	// refresh: function(frm) {

	// }
	refresh: function(frm) {
		frm.fields_dict['pick_locker_trainer'].grid.get_field('service_locker').get_query = function(){
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
});

function getExisted(frm2)
{
	console.log('getExisted()');
	console.log(frm2);
	var pick_locker_trainer = frm2.doc.pick_locker_trainer;
	var arrcurrent_pick_locker = [];
	for(var i=0;i<pick_locker_trainer.length;i++)
	{
		var tr = pick_locker_trainer[i].service_locker;
		if (tr!=undefined) arrcurrent_pick_locker.push(tr);
	}
	console.log(arrcurrent_pick_locker)
	return arrcurrent_pick_locker;
}