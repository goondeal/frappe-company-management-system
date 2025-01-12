# Copyright (c) 2025, salamouny and contributors
# For license information, please see license.txt

from datetime import date, datetime
import frappe
from frappe.model.document import Document
from frappe.utils.password import update_password


class Employee(Document):
    @property
    def days_employed(self):
        if self.hired_on:
            print('hired_on', self.hired_on)
            hiring_date = self.hired_on
            if isinstance(self.hired_on, str):
                hiring_date = datetime.strptime(
                    self.hired_on, '%Y-%m-%d').date()
            return (date.today() - hiring_date).days

    def validate(self):
        user = frappe.session.user
        if user == "Administrator":
            return
        roles = frappe.get_roles(user)
        if "Manager" in roles and self.role == "Admin":
            frappe.throw("You do not have permission to create an Admin user")
            return
        user_company = frappe.get_value("Employee", {"email": user}, "company")
        if user_company != self.company:
            frappe.throw(
                "You do not have permission to create an Employee for another company")
            return
    # before insert create a user for this employee

    def before_insert(self):
        if not frappe.db.exists("Employee", {"email": self.email}):
            user = frappe.get_doc({
                "doctype": "User",
                "first_name": self.employee_name.split()[0],
                "last_name": ''.join(self.employee_name.split()[1:]),
                "email": self.email,
                "phone": self.mobile_number,
                "enabled": 1,
                "new_password": self.password,
                # Assign the default Employee role
                "roles": [{"role": self.role}],
            })
            user = user.insert(ignore_permissions=True)
            # update_password(user.name, self.password, logout_all_sessions=True)
            frappe.msgprint(
                f"User created for Employee: {self.employee_name} ({self.email})")

    # on update update the user for this employee
    def on_update(self):
        if self.is_new():
            return
        emp = self.get_doc_before_save()
        if emp:
            user = frappe.get_doc("User", emp.email)
            fn, *ln = self.employee_name.split(" ")
            if user.first_name != fn:
                user.first_name = fn
            if user.last_name != ''.join(ln):
                user.last_name = ''.join(ln)
            if user.email != self.email:
                user.email = self.email
            if user.phone != self.mobile_number:
                user.phone = self.mobile_number
            if emp.role != self.role:
                user.roles = []
                user.append("roles", {"role": self.role})
                
            if emp.password != self.password:
                print('============updating password', self.password, emp.password)
                update_password(user.name, self.password,
                                logout_all_sessions=False)
            user.save(ignore_permissions=True)
            frappe.msgprint(
                f"User updated for Employee: {self.employee_name} ({self.email})")

    # on delete delete the user for this employee
    def on_trash(self):
        user = frappe.get_doc("User", self.email)
        user.delete(ignore_permissions=True)
        frappe.msgprint(
            f"User deleted for Employee: {self.employee_name} ({self.email})")
