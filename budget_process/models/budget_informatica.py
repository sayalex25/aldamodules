from odoo import fields, models


class BudgetInformatica(models.Model):
    _name = "budget.informatica"
    _description = "IT budget"
    _inherit = "budget.base"
    department = fields.Selection(
        [("informatica", "Informática")],
        default="informatica",
        readonly=True,
    )
