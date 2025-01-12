# Copyright (c) 2025, salamouny and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PerformanceReview(Document):
	# set company field value from user on creation
    def validate(self):
        print("employee", self.employee)
        emp = frappe.get_doc("Employee", self.employee)
        self.company = emp.company
        self.department = emp.department
