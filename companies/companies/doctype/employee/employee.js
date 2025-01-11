// Copyright (c) 2025, salamouny and contributors
// For license information, please see license.txt

// validate email
function validateEmail(email) {
    return frappe.utils.validate_type(email, "email");
}
// validate phone
function validatePhone(phone) {
    return frappe.utils.validate_type(phone, "phone");
}
frappe.ui.form.on("Employee", {
    refresh(frm) {

    },
    // validate email and phone before submitting
    validate: function (frm) {
        if (frm.doc.email) {
            if (!validateEmail(frm.doc.email)) {
                frappe.msgprint(__("Invalid Email Address"));
                frappe.validated = false;
            }
        }
        if (frm.doc.mobile_number) {
            if (!validatePhone(frm.doc.mobile_number)) {
                frappe.msgprint(__("Invalid Mobile Number"));
                frappe.validated = false;
            }
        }
    },
    company: function(frm) {
        frm.set_query('department', function() {
            return {
                filters: {
                    company: frm.doc.company
                }
            };
        });
    },
});
