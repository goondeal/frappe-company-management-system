app_name = "companies"
app_title = "Companies"
app_publisher = "salamouny"
app_description = "Company Management System"
app_email = "ahmed.salamony497@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/companies/css/companies.css"
# app_include_js = "/assets/companies/js/companies.js"

# include js, css files in header of web template
# web_include_css = "/assets/companies/css/companies.css"
# web_include_js = "/assets/companies/js/companies.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "companies/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "companies/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "companies.utils.jinja_methods",
# 	"filters": "companies.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "companies.install.before_install"
# after_install = "companies.install.after_install"

after_install = "companies.after_install.create_roles"

# Uninstallation
# ------------

# before_uninstall = "companies.uninstall.before_uninstall"
# after_uninstall = "companies.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "companies.utils.before_app_install"
# after_app_install = "companies.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "companies.utils.before_app_uninstall"
# after_app_uninstall = "companies.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "companies.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

permission_query_conditions = {
    "Employee": "companies.employee_permissions.get_permission_query_conditions",
    "Company": "companies.company_permissions.get_permission_query_conditions",
    "Department": "companies.department_permissions.get_permission_query_conditions",
    "Project": "companies.project_permissions.get_permission_query_conditions",
    "Performance Review": "companies.performance_review_permissions.get_permission_query_conditions",
}

has_permission = {
    "Employee": "companies.employee_permissions.has_permission",
    "Company": "companies.company_permissions.has_permission",
    "Department": "companies.department_permissions.has_permission",
    "Project": "companies.project_permissions.has_permission",
    "Performance Review": "companies.performance_review_permissions.has_permission",
}

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"companies.tasks.all"
# 	],
# 	"daily": [
# 		"companies.tasks.daily"
# 	],
# 	"hourly": [
# 		"companies.tasks.hourly"
# 	],
# 	"weekly": [
# 		"companies.tasks.weekly"
# 	],
# 	"monthly": [
# 		"companies.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "companies.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "companies.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "companies.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["companies.utils.before_request"]
# after_request = ["companies.utils.after_request"]

# Job Events
# ----------
# before_job = ["companies.utils.before_job"]
# after_job = ["companies.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"companies.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

