from odoo import fields, models


class BudgetOperaciones(models.Model):
    _name = "budget.operaciones"
    _description = "Operations budget"
    _inherit = "budget.base"
    department = fields.Selection(
        [("operaciones", "Operaciones")],
        default="operaciones",
        readonly=True,
    )
