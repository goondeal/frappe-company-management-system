# Copyright (c) 2025, salamouny and contributors
# For license information, please see license.txt

from datetime import date, datetime
from frappe.model.document import Document


class Employee(Document):
    @property
    def days_employed(self):
        if self.hired_on:
            print('hired_on', self.hired_on)
            hiring_date = self.hired_on
            if isinstance(self.hired_on, str):
                hiring_date = datetime.strptime(
                    self.hired_on, '%Y-%m-%d').date()
            return(date.today() - hiring_date).days
