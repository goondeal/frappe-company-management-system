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
    async setup(frm) {
        try {
            var company = await frappe.db.get_value("Employee", { email: frappe.session.user }, "company");
            if (company?.message?.company) {
                frm.set_query('company', function () {
                    return {
                        filters: {
                            name: company?.message?.company
                        }
                    };
                });
            }
        } catch (error) {
            console.log(error);
        }

    },
    refresh(frm) {

    },
    // validate email and phone before submitting
    validate: async function (frm) {
        // Check if the user already has an employee record
        // check only when creation
        // if (!frm.doc.name) {
        //     try {
        //         var emp = await frappe.db.get_list("Employee", { filters: { "user": frm.doc.user } });
        //         if (emp.length > 0) {
        //             frappe.msgprint(__("User already has an Employee record"));
        //             frappe.validated = false;
        //         }
        //     } catch (error) {
        //         console.log(error);
        //     }
        // }
        // TODO: check if the choosen department belongs to the choosen company

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
    company: function (frm) {
        // clear department field value
        frm.set_value("department", "");
        frm.set_query('department', function () {
            return {
                filters: {
                    company: frm.doc.company
                }
            };
        });
    },
    // if user is changed, then set the user's email and mobile number
    // user: function (frm, cdt, cdn) {
    //     if (frm.doc.user) {
    //         frappe.db.get_doc("User", frm.doc.user).then(data => {
    //             frm.set_value("email", data.email);
    //             frm.set_value("mobile_number", data.phone);
    //             frm.set_value("employee_name", `${data.first_name || ""} ${data.last_name || ""}`);
    //             console.log(data.email);
    //         });
    //     }
    // },
});
