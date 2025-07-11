from odoo import fields, models


class BudgetTAZ(models.Model):
    _name = "budget.taz"
    _description = "TAZ budget"
    _inherit = "budget.base"
    department = fields.Selection(
        [("taz", "Presupuestos TAZ")], default="taz", readonly=True
    )
