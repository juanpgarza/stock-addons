# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api

class StockReturnPickingReason(models.Model):
	_name = 'stock.return.picking.reason'
	_description = 'Motivo de devolución'

	name = fields.Char('Descripción')