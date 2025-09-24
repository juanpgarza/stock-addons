# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    reason_id = fields.Many2one(comodel_name="stock.return.picking.reason", string= 'Motivo de devolución')

    # def _create_returns(self):
    #     # add to new picking for return the reason for the return
    #     new_picking, pick_type_id = super()._create_returns()
    #     picking = self.env['stock.picking'].browse(new_picking)
    #     picking.write({'reason_id': self.reason_id.id})

    #     return new_picking, pick_type_id

    def _create_return(self):
        # add to new picking for return the reason for the return
        new_picking = super()._create_return()
        new_picking.write({'reason_id': self.reason_id.id})
        # import pdb; pdb.set_trace()
        return new_picking