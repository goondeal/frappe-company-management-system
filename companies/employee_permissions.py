import frappe


def get_permission_query_conditions(user):
    roles = frappe.get_roles(user)
    if user == "Administrator":
        return ""
    print('roles', roles)
    if "Admin" in roles:
        # Get the company associated with the user
        company = frappe.get_value("Employee", {"email": user}, "company")
        if company:
            return f"`tabEmployee`.`company` = '{company}'"
    if "Manager" in roles:
        # Get the company associated with the user
        department = frappe.get_value("Employee", {"email": user}, "department")
        if department:
            return f"`tabEmployee`.`department` = '{department}'"
    if "Employee" in roles:
        return f"`tabEmployee`.`user` = '{user}'"
    return ""


def has_permission(doc, user):
    # Allow access if the employee belongs to the same company
    roles = frappe.get_roles(user)
    if user == "Administrator":
        return True
    if "Admin" in roles or "Manager" in roles:
        user_employee_company = frappe.get_value(
            "Employee", {"email": user}, "company")
        return doc.company == user_employee_company
    return doc.email == user
