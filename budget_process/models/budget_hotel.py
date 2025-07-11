from odoo import fields, models


class BudgetHotel(models.Model):
    _name = "budget.hotel"
    _description = "Hotel"

    name = fields.Char(required=True)
    code = fields.Char()
