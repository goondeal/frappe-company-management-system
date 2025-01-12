import frappe


def get_permission_query_conditions(user):
    roles = frappe.get_roles(user)
    if user == "Administrator":
        return ""
    if "Admin" in roles:
        company = frappe.get_value("Employee", {"email": user}, "company")
        return f"`tabDepartment`.`company` = '{company}'"
    if "Manager" in roles or "Employee" in roles:
        department = frappe.get_value("Employee", {"email": user}, "department")
        if department:
            return f"`tabDepartment`.`name` = '{department}'"
    return ""


def has_permission(doc, user):
    roles = frappe.get_roles(user)
    if user == "Administrator":
        return True
    if "Admin" in roles:
        user_employee_company = frappe.get_value(
            "Employee", {"email": user}, "company")
        return doc.company == user_employee_company
    if "Manager" in roles or "Employee" in roles:
        user_employee_department = frappe.get_value(
            "Employee", {"email": user}, "department")
        return doc.name == user_employee_department
    return False
