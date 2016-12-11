# -*- coding: utf-8 -*-
from openerp import models, fields, api,_

class BackendMandanten(models.Model):
    _name='res.partner'
    _inherit=['res.partner','mail.thread']
    _inherits={'backend.mandanten':'backendmandant_id'}
    backendmandant_id=fields.Many2one('backend.mandanten', required=True, ondelete='cascade', index=True)
 
    ist_mandant=fields.Boolean('Ist Mandant')
    contact_id=fields.Many2one('backend.kontakte', string='Contact ID')
    bank_rel=fields.One2many('bank.detail', 'mandant_id')
    order_id=fields.One2many('client.order', 'client_order_id')
    number_id=fields.One2many('client.number', 'name')
    ticketing_rel=fields.One2many('felix1.ticket','priPriority_id')
    branch_id=fields.One2many('backend.kanzleien','branch')
    partner_id=fields.Many2one('res.partner')
    
