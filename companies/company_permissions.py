import frappe


def get_permission_query_conditions(user):
    company = frappe.get_value("Employee", {"email": user}, "company")
    if company:
        return f"`tabCompany`.`name` = '{company}'"
    return ""


def has_permission(doc, user):
    # Allow access if the user belongs to the company
    user_employee_company = frappe.get_value(
        "Employee", {"email": user}, "company")
    return doc.name == user_employee_company
