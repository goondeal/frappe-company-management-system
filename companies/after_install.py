import frappe

def create_roles():
    """
    Create roles during app installation.
    """
    roles = ["Admin", "Manager", "Employee"]
    for role in roles:
        if not frappe.db.exists("Role", role):  # Check if the role already exists
            frappe.get_doc({
                "doctype": "Role",
                "role_name": role,
                "desk_access": 1,
            }).insert(ignore_permissions=True)
            frappe.msgprint(f"Role '{role}' has been created.")
