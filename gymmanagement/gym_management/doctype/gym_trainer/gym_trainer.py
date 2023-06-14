# Copyright (c) 2023, Mr Ameen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class GymTrainer(Document):
	def on_update(self):
		print(f'\n\nGymMembership on_update() {self.pick_locker_trainer} \n\n')
		checklocker(self)
		
		
	
	
	
def checklocker(self):
	arrlocker = self.pick_locker_trainer
	old_doc = self.get_doc_before_save()
	if old_doc is not None:
		old_arrlocker = old_doc.pick_locker_trainer
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
			doc.last_user_used = self.user_trainer
			doc.last_date = datetime.now()
			doc.save()
			print('Done update Not:',locker_name)
			doc.reload()
	
	

