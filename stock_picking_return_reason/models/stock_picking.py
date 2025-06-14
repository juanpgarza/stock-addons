# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ProntoStockPicking(models.Model):
    _inherit = 'stock.picking'

    reason_id = fields.Many2one(comodel_name="stock.return.picking.reason", string= 'Motivo de devolución')
