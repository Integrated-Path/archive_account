from odoo import models, fields, api

class AccountAccount(models.Model):
	_inherit = "account.account"

	active = fields.Boolean("Active", default=True, copy=False, readonly=True)