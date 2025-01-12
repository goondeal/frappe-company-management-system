import frappe


def get_permission_query_conditions(user):
    if user == "Administrator":
        return ""
    roles = frappe.get_roles(user)
    if "Admin" in roles:
        company = frappe.get_value("Employee", {"user": user}, "company")
        return f"`tabProject`.`company` = '{company}'"
    if "Manager" in roles or "Employee" in roles:
        department = frappe.get_value("Employee", {"user": user}, "department")
        if department:
            return f"`tabProject`.`department` = '{department}'"
    return ""


def has_permission(doc, user):
    if user == "Administrator":
        return True
    roles = frappe.get_roles(user)
    if "Admin" in roles:
        user_employee_company = frappe.get_value(
            "Employee", {"user": user}, "company")
        return doc.company == user_employee_company
    if "Manager" in roles or "Employee" in roles:
        user_employee_department = frappe.get_value(
            "Employee", {"user": user}, "department")
        return doc.department == user_employee_department
    return False
