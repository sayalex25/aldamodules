from odoo import fields, models


class BudgetCAPEX(models.Model):
    _name = "budget.capex"
    _description = "CAPEX budget"
    _inherit = "budget.base"
    department = fields.Selection([("capex", "CAPEX")], default="capex", readonly=True)
