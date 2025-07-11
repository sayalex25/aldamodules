from odoo import fields, models


class BudgetCFO(models.Model):
    _name = "budget.cfo"
    _description = "CFO budget"
    _inherit = "budget.base"
    department = fields.Selection([("cfo", "CFO")], default="cfo", readonly=True)
