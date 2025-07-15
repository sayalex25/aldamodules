from odoo import fields, models


class BudgetRevenue(models.Model):
    _name = "budget.revenue"
    _description = "Revenue budget"
    _inherit = "budget.base"
    department = fields.Selection(
        [("revenue", "Revenue")], default="revenue", readonly=True
    )
