from odoo import fields, models


class BudgetMarketing(models.Model):
    _name = "budget.marketing"
    _description = "Marketing budget"
    _inherit = "budget.base"
    department = fields.Selection(
        [("marketing", "Marketing")],
        default="marketing",
        readonly=True,
    )
