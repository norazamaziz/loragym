// Copyright (c) 2023, Mr Ameen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Subscription Plan', {
	
	refresh: function(frm) {
		// this for table, not used anymore
		// frm.fields_dict['trainer_child_plan'].grid.get_field('trainers').get_query = function(){
		// 	return {
		// 		filters:[
		// 			['Gym Trainer','user_trainer','not in',getUserExist(frm)]
		// 		]
		// 	}
		// };
		cur_frm.fields_dict['plan_name'].get_query = function(doc) {
			return {
				filters: {
					"plan_type": 'Standard'
				}
			}
		};
		
		cur_frm.fields_dict['trainer_user'].get_query = function(doc) {
			return {
				filters: {
					"type_trainer": 'Gym'
				}
			}
		};
		
	},
});

function getUserExist(frm2){
	// console.log('start getUserExist()')
	// console.log(frm2)
	var trainer_child_plan = frm2.doc.trainer_child_plan;
	// console.log(trainer_child_plan);
	var arrcurrent_trainer_child_plan = [];
	for(var i=0;i<trainer_child_plan.length;i++)
	{
		var tr = trainer_child_plan[i].trainers;
		if (tr!=undefined) arrcurrent_trainer_child_plan.push(tr);
	}
	// console.log('arrcurrent_trainer_child_plan');
	// console.log(arrcurrent_trainer_child_plan);
	// var arr = [];
	// // NO NEED CALL BACKEND
	frappe.call({
		method:'gym_management.services.rest.getMemberExist',
		args: {
			'typeuser': 'trainer',
			'id': frm2.doc.name,
		},
		async: false,
		callback: function(r) {
			//
			arr = r.message.arr;
			// console.log('arr atas');
			// console.log(arr);
			// return arr;
		}
	});
	// // console.log('arr bawah');
	// // console.log(arr);
	// arr.push(arrcurrent_trainer_child_plan);
	return arrcurrent_trainer_child_plan;
}

