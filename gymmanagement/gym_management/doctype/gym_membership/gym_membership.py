# Copyright (c) 2023, Mr Ameen and contributors
# For license information, please see license.txt

import frappe, random
from frappe.model.document import Document
from datetime import datetime

class GymMembership(Document):
	def before_insert(self):
		exists = frappe.db.exists(
            "Gym Trainer Child",
            {
                "training": self.user_membership,
                "status_plan": 'Active',
                # check if the membership's end date is later than this membership's start date
                # "end_plan": (">", self.start_plan)
            },
        )
		if exists:
			frappe.throw("There is an active membership for this member")
		rd = str(random.randint(0,1000000))
		print('\n\nbefore_insert() .py random ticket number:',rd,'\n\n')
		self.subscription_no = self.user_membership+'-'+rd
			


	def on_update(self):
		print(f'\n\nGymMembership on_update() {self.pick_locker_membership} \n\n')
		checklocker(self)
		
		
	
	
	
def checklocker(self):
	arrlocker = self.pick_locker_membership
	old_doc = self.get_doc_before_save()
	if old_doc is not None:
		old_arrlocker = old_doc.pick_locker_membership
		print(f'\n\nOld: {len(old_arrlocker)} , New: {len(arrlocker)}')
		for z in old_arrlocker: # First update as available
			locker_name = z.service_locker
			found = False
			for x in arrlocker:
				locker_name_new = x.service_locker
				if locker_name == locker_name_new:
					found = True
					break
			if found==False:
				doc = frappe.get_doc("Gym Locker",locker_name)
				doc.status = 'Availaible'
				doc.save()
				doc.reload()
				z.delete()
				print('Done update Availaible:',locker_name)

		count = 0
		for x in arrlocker:
			count += 1
			locker_name = x.service_locker
			print(f'locker_name:{locker_name}')
			if count > 2:
				# Limit 2 only
				# frappe.throw("Max locker can book 2 only")
				frappe.msgprint('Max locker can book 2 only')
				x.delete()
				print('done delete:',locker_name)
				self.reload()
				return
			doc = frappe.get_doc("Gym Locker",locker_name)
			doc.status = 'Not Availaible'
			doc.last_user_used = self.user_membership
			doc.last_date = datetime.now()
			doc.save()
			print('Done update Not:',locker_name)
			doc.reload()
	
	
