# Copyright (c) 2025, salamouny and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Department(Document):
    @property
    def number_of_employees(self):
        return frappe.db.count('Employee', filters={'department': self.name})

    @property
    def number_of_projects(self):
        return frappe.db.count('Project', filters={'department': self.name})
