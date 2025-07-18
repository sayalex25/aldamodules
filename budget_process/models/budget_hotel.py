# Copyright 2025 Alexandra Suarez Graterol (Alda hotels) <saya.alex20@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class BudgetHotel(models.Model):
    _name = "budget.hotel"
    _description = "Budget Hotel Management"
    _inherit = "budget.base"

    department = fields.Selection(
        [("Hotels", "Hotels")],
        default="Hotels",
        readonly=True,
    )
