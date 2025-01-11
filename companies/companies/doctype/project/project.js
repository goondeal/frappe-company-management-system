// Copyright (c) 2025, salamouny and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project', {
    company: function(frm) {
        frm.set_query('department', function() {
            return {
                filters: {
                    company: frm.doc.company
                }
            };
        });
    },
    department: function(frm) {
        frm.set_query('assigned_employees', function() {
            return {
                filters: {
                    department: frm.doc.department
                }
            };
        });
    }
});
