from odoo import fields, models


class BudgetController(models.Model):
    _name = "budget.controller"
    _description = "Controller budget"
    _inherit = "budget.base"
    department = fields.Selection(
        [("controller", "Controller")],
        default="controller",
        readonly=True,
    )
