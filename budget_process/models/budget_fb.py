from odoo import fields, models


class BudgetFB(models.Model):
    _name = "budget.fb"
    _description = "F&B budget"
    _inherit = "budget.base"
    department = fields.Selection(
        [("fb", "Food & Beverage")], default="fb", readonly=True
    )
