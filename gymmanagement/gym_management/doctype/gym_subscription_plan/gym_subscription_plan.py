# Copyright (c) 2023, Mr Ameen and contributors
# For license information, please see license.txt

import frappe
from frappe import _, scrub, throw
from frappe.website.website_generator import WebsiteGenerator
# from frappe.model.document import Document

class GymSubscriptionPlan(WebsiteGenerator):

	def on_update(self):
		print(f'\n\n GymSubscriptionPlan on_update() \n\n')
		# self.validate_duplicate_user_id()
		
	pass

	# def validate(self):
	# 	self.validate_duplicate_user_id()
	# 	pass

	# Doctype deleted
	# def validate_duplicate_user_id(self):
	# 	print('self.name:',self.name)
	# 	obj = frappe.db.get_all('Gym Trainer Child Plan',filters={'parent':self.name},fields=['name','trainers','full_name'])
	# 	arrtrainer = []
	# 	for x in obj:
	# 		trainer = x.trainers
	# 		print(f'\n\n{x.name} x:{x.full_name},trainers:{trainer}')
	# 		for t in arrtrainer:
	# 			if t == trainer:
	# 				print('Already exist, delete it')
	# 				frappe.delete_doc("Gym Trainer Child Plan", x.name)
	# 				self.reload()
	# 				throw(
	# 					_("Trainer is already assigned to this plan"),
	# 					# _("User {0} is already assigned to Trainer {1}").format(self.plan_user3, train[0][0]),
	# 					frappe.DuplicateEntryError,
	# 				)
	# 		arrtrainer.append(x.trainers)
		# if(len(self.plan_user3)>0):
		# 	print(f'self.plan_user3:{self.plan_user3[0].trainers} \nself.plan_name:{self.plan_name}')
		# 	Trainer = frappe.qb.DocType("Gym Subscription Plan")
		# 	train = (
		# 		frappe.qb.from_(Trainer)
		# 		.select(Trainer.plan_user3)
		# 		.where(
		# 			(Trainer.plan_user3 == self.plan_user3[0].trainers)
		# 			& (Trainer.plan_name != self.plan_name)
		# 		)
		# 	).run()

		# 	# if train:
		# 	# 	throw(
		# 	# 		_("User is already assigned to Trainer"),
		# 	# 		# _("User {0} is already assigned to Trainer {1}").format(self.plan_user3, train[0][0]),
		# 	# 		frappe.DuplicateEntryError,
		# 	# 	)

		# 	train2 = (
		# 		frappe.qb.from_(Trainer)
		# 		.select(Trainer.plan_user3,Trainer.plan_name)
		# 		.where(
		# 			(Trainer.plan_user3 == self.plan_user3[0].trainers)
		# 			& (Trainer.plan_name == self.plan_name)
		# 		)
		# 	).run()
		# 	# if train2:
		# 	# 	count = 0
		# 	# 	for x in train2:
		# 	# 		count += 1
		# 	# 		print(f'{count}: x:{x[0],x[1]}')
		# 	# 		print(f'{count}: self:{self.plan_name,self.plan_user3[0].trainers}\n\n')
		# 	# 		if x[1]==self.plan_name and x[0]==self.plan_user3[0].trainers:
		# 	# 			throw(
		# 	# 				_("User is already assigned to this plan"),
		# 	# 				# _("User {0} is already assigned to Trainer {1}").format(self.plan_user3, train[0][0]),
		# 	# 				frappe.DuplicateEntryError,
		# 	# 			)
		# 	# 			break
