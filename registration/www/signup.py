from __future__ import unicode_literals
import frappe
# from central.utils import get_signup_domain

def get_context(context):
	return {
		# 'signup_domain': get_signup_domain() or 'punia.online'
		'signup_domain': 'digitalprizm.net'
	}
