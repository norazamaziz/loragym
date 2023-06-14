# Copyright (c) 2023, Mr Ameen and contributors
# For license information, please see license.txt

# import frappe
from datetime import datetime
from frappe.model.document import Document

class GymFitnessProfile(Document):
	pass


	def on_update(self):
		print(f'\n\nGymFitnessProfile on_update()')
		# Handle client script
		# now = datetime.now()
		# today1 = now.strftime("%Y-%m-%d %H:%M:%S")
		# print('today:',today1)
		# self.dateupdated = today1
		