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
            return f"`tabPerformance Review`.`company` = '{company}'"
    if "Manager" in roles:
        # Get the department associated with the user
        department = frappe.get_value(
            "Employee", {"email": user}, "department")
        print("department", department)
        if department:
            return f"`tabPerformance Review`.`department` = '{department}'"
    if "Employee" in roles:
        name = frappe.get_value("Employee", {"email": user}, "name")
        return f"`tabPerformance Review`.`employee` = '{name}'"
    return ""


def has_permission(doc, user):
    # Allow access if the employee belongs to the same company
    roles = frappe.get_roles(user)
    if user == "Administrator":
        return True
    if "Admin" in roles:
        company = frappe.get_value(
            "Employee", {"email": user}, "company")
        return not doc.company or doc.company == company
    if "Manager" in roles:
        department = frappe.get_value(
            "Employee", {"email": user}, "department")
        return not doc.department or doc.department == department
    return False
