import frappe, random
from frappe.utils import getdate
from frappe.utils import today
from datetime import datetime # from python std library
from frappe.utils import add_to_date

def getrandom():
    rd = str(random.randint(0,1000000))
    return rd

@frappe.whitelist()
def getMemberExist(typeuser,id):
    print('\n\n\ngetMemberExist() \ntypeuser:',typeuser)
    if typeuser == 'trainer':
        obj = frappe.db.get_all('Gym Trainer Child Plan',filters={'parent':id},fields=['name','trainers','full_name'])
        arrtrainerExisted = []
        for x in obj:
            trainer = x.trainers
            print(f'\n\n{x.name} x:{x.full_name},trainers:{trainer}')
            arrtrainerExisted.append(x.trainers)

    data = {
        'arr': arrtrainerExisted
    }
    return data


def checkMembership(name):
    print('checkMembership(name):',name)
    # obj = frappe.db.get_all('Gym Membership',filters={'name':name},fields=[])
    obj = frappe.db.get_list('Gym Membership', filters={
        'user_membership': ['=', name],
        # 'status': ['=', 'Active'],
    },fields=['status'])
    print(obj)
    if obj:
        return True
    return False

def checkMembershipActive(name):
    print('checkMembership(name):',name)
    # obj = frappe.db.get_all('Gym Membership',filters={'name':name},fields=[])
    obj = frappe.db.get_list('Gym Membership', filters={
        'user_membership': ['=', name],
        'status': ['=', 'Active'],
    },fields=['status'])
    print(obj)
    if obj:
        return True
    return False

def checkTrainerChild(name):
    print('checkTrainerChild(name):',name)
    obj = frappe.db.get_all('Gym Trainer Child',filters={'training':name},fields=[])
    # obj = frappe.db.get_list('Gym Trainer Child', filters={
    #     'training': ['=', name]
    # })
    print(obj)
    if obj:
        return True
    return False

@frappe.whitelist()
def create_gym_membership(plan_name,trainer_user,plan_price,plan_duration,plan_type,count_subscription):
    currentuser = frappe.get_user().doc
    full_name = currentuser.full_name
    name = currentuser.name
    doctypeplanname = ''
    if plan_type == 'professional':
        doctypeplanname = 'Gym Professional Trainer Plan'
    else:
        doctypeplanname = 'Gym Subscription Plan'

    print('\n\n\ncreate_gym_membership() \nplan_name:',plan_name,'fullname:',full_name,'trainer_user:',trainer_user)
    print('name:',name)
    # print(getdate())
    # print(today())
    month = 0
    if 'Month' in plan_duration:
        splt = plan_duration.split(' ')
        month = int(splt[0])
    elif 'Year' in plan_duration:
        splt = plan_duration.split(' ')
        month = int(splt[0])*12
    after_plan_duration = add_to_date(datetime.now(), months=month, as_string=True)
    print('after_plan_duration:',after_plan_duration)
    subscription_no1 = getrandom()
    subscription_no = name+'-'+subscription_no1

    # CHECK MEMBERSHIP ACTIVE ALREADY EXIST  
    # before_insert(name)
    # CREATE MEMBERSHIP IF NOT EXIST
    bolmem = checkMembership(name) # NO NEED already check function before_insert
    print('Membership bolmem:',bolmem)
    if bolmem == False:
        jsonmembership = {
            "doctype": "Gym Membership",
            "user_membership": name,
            "full_name": full_name,
            "status": "Active",
            "start_plan": today(),
            "end_plan": after_plan_duration,
            "subscription_no": subscription_no
        }
        if plan_type == 'professional':
            jplt = {
                'pro_plan': plan_name
            }
        else:
            jplt = {
                'member_plan': plan_name
            }
        jsonmembership.update(jplt)
        doc = frappe.get_doc(jsonmembership)
        doc.insert()
        print('Done create NEW MEMBERSHIP')
    else:
        bolmemActv = checkMembershipActive(name)
        if bolmemActv == False:
            jsonmembership = {
                "status": "Active",
                "start_plan": today(),
                "end_plan": after_plan_duration,
                "subscription_no": subscription_no
            }
            if plan_type == 'professional':
                jplt = {
                    'pro_plan': plan_name
                }
            else:
                jplt = {
                    'member_plan': plan_name
                }
            jsonmembership.update(jplt)
            # Update status
            frappe.db.set_value('Gym Membership', name, jsonmembership)
            print('\nDone update membership to ACTIVE and others')
            # return False
        else:
            frappe.throw("There is an active membership for this member")

    # CREATE GYM TRAINER CHILD TO ASSIGNED MEMBERSHIP UNDER TRAINER
    boltrainerchld = checkTrainerChild(name)
    if boltrainerchld == False:
        jsondoctrainerchild = {
            "doctype": "Gym Trainer Child",
            "training": name,
            "name1": full_name,
            "parent": trainer_user,
            "parentfield":"gym_training",
            "parenttype":"Gym Trainer",
        }
        if plan_type == 'professional':
            pnm = {
                "plan_pro": plan_name
            }
        else:
            pnm = {
                "plan": plan_name,
            }
        jsondoctrainerchild.update(pnm)

        doc = frappe.get_doc(jsondoctrainerchild)
        doc.insert()

    # CREATE CUSTOMER FOR SALES INVOICE
    doc = frappe.get_doc({
        "docstatus": 0,
        "doctype": "Customer",
        "customer_type": "Company",
        "customer_name": subscription_no,
        "customer_group": "Commercial",
        "territory": "Malaysia"
    })
    doc.insert()
    
    # CREATE GYM ITEM CHILD FOR SALES INVOICE
    # CREATE INVOICE FOR REPORT
    items = []
    a = {
        "item_code": plan_name,
        "qty": 1,
        "rate": plan_price,
    }
    items.append(a)
    sales_invoice = frappe.get_doc({
        "doctype": "Sales Invoice",
        "customer": subscription_no,
        "due_date": frappe.utils.nowdate(),
        "subscription_no": subscription_no,
        "items":items
    })
    sales_invoice.insert()
    # sales_invoice.submit() # auto submit
    frappe.db.commit() # save into db

    # UPDATE COUNT SUBSCRIPTION +1
    cntsub = 1 + checkint(count_subscription)
    frappe.db.set_value(doctypeplanname, plan_name, {
        'count_subscription': cntsub
    })
    return 'success'

# check membership already exist and active or not 
def before_insert(name):
    exists = frappe.db.exists(
        "Gym Membership",
        {
            "user_membership": name,
            "status":("=", 'Active'),
            # check if the membership's end date is later than this membership's start date
            # "end_plan": (">", self.start_plan)
        },
    )
    if exists:
        frappe.throw("There is an active membership for this member")

def checkint(c):
    try:
        c = int(c)
    except:
        c = 0
    return c

@frappe.whitelist()
def getCaloriesburned(exr):
    print('\n\n getCaloriesburned:',exr)
    obj = frappe.db.get_all('Gym Activity',filters={'name':exr},fields=['calories_burned'])
    calories_burned = obj[0]['calories_burned']
    print(calories_burned)
    return calories_burned
