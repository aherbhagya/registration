# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "registration"
app_title = "Registration"
app_publisher = "Digitalprizm"
app_description = "Manages registration"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "contact@digitalprizm.net"
app_license = "MIT"

# Includes in <head>
# ------------------
hide_in_installer = True

website_context = {
	"hide_login": 1,
	"favicon": "/assets/registrationdemo/img/favicon.ico",
	"disable_website_theme": True
}
# include js, css files in header of desk.html
# app_include_css = "/assets/registration/css/registration.css"
# app_include_js = "/assets/registration/js/registration.js"
web_include_css = ["assets/frappe/css/hljs.css"]
web_include_js = [
	"/assets/frappe/js/lib/highlight.pack.js",
	"/assets/registrationdemo/js/payment.js"
	]
# include js, css files in header of web template
# web_include_css = "/assets/registration/css/registration.css"
# web_include_js = "/assets/registration/js/registration.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"
home_page = "index"
# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "registration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "registration.install.before_install"
# after_install = "registration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "registration.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"registration.tasks.all"
# 	],
# 	"daily": [
# 		"registration.tasks.daily"
# 	],
# 	"hourly": [
# 		"registration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"registration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"registration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "registration.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "registration.event.get_events"
# }

