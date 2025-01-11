# Copyright (c) 2025, salamouny and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Company(Document):
    @property
    def number_of_departments(self):
        return frappe.db.count('Department', filters={'company': self.name})

    @property
    def number_of_employees(self):
        return frappe.db.count('Employee', filters={'company': self.name})

    @property
    def number_of_projects(self):
        return frappe.db.count('Project', filters={'company': self.name})
