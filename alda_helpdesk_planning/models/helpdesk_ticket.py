from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    date_planned_start = fields.Datetime(
        string="Fecha de inicio planificada",
        help="Fecha y hora en la que el TMZ planifica empezar a atender esta incidencia.",
        tracking=True,
    )
    date_planned_end = fields.Datetime(
        string="Fecha de fin planificada",
        help="Fecha y hora en la que el TMZ planifica terminar de atender esta incidencia.",
        tracking=True,
    )
