from odoo import models, fields, api
from odoo.exceptions import UserError

class ChangePickingtypeWizard(models.TransientModel):
    _name = 'change.picking.type.wizard'
    _description = 'Cambiar el tipo de operación'

    picking_id = fields.Many2one('stock.picking')

    picking_type_id = fields.Many2one('stock.picking.type', string='Tipo')

    @api.model
    def default_get(self, field_names):
        defaults = super(
            ChangePickingtypeWizard, self).default_get(field_names)
        defaults['picking_id'] = self.env.context['active_id']
        return defaults

    def do_update(self):        

        # if self.picking_id.state != 'draft':
        #     raise UserError("Solo en borrador")

        if self.picking_id.picking_type_id.id == self.picking_type_id.id:
            raise UserError("Indique un tipo de operación distinto al actual")

        if self.picking_id.picking_type_id.code != self.picking_type_id.code:
            if self.picking_id.picking_type_id.code == 'outgoing':
                msg = "Debe informar un tipo de operacion de entrega"
            else:
                msg = "Debe informar un tipo de operacion de recepción"

            raise UserError(msg)       
        
        if self.picking_id.move_ids_without_package.filtered(lambda x: x.state == 'cancel'):
            raise UserError("La operación tiene movimientos cancelados. Debe eliminarlos para poder hacer el cambio.")

        # el campo qty_done se elimina en v17 https://github.com/OCA/OpenUpgrade/blob/a325c03a9530246f9a6a39320e2c2815c04a7050/openupgrade_scripts/scripts/stock/17.0.1.1/upgrade_analysis.txt#L28        
        # self.picking_id.move_line_ids.filtered(lambda x: x.state not in ['draft', 'done', 'cancel']).write({'qty_done': False})
        self.picking_id.action_cancel()
        self.picking_id.action_back_to_draft()

        if self.picking_type_id.code == 'outgoing':
            self.picking_id.write(
                {
                'name': self.picking_type_id.sequence_id.next_by_id(),
                'picking_type_id': self.picking_type_id.id,
                'location_id': self.picking_type_id.default_location_src_id.id,            
                }
            )
        else:
            self.picking_id.write(
                {
                'name': self.picking_type_id.sequence_id.next_by_id(),
                'picking_type_id': self.picking_type_id.id,
                'location_dest_id': self.picking_type_id.default_location_dest_id.id,            
                }
            )

        self.picking_id.action_confirm()
        self.picking_id.action_assign()

        for move in self.picking_id.move_ids_without_package:
            if self.picking_type_id.code == 'outgoing':
                move.write(
                    {
                        'location_id': self.picking_type_id.default_location_src_id.id,
                    }
                )
            else:
                move.write(
                    {
                        'location_dest_id': self.picking_type_id.default_location_dest_id.id,
                    }
                )
