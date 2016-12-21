# -*- coding: utf-8 -*-
from openerp import models, fields, api,_

class BackendMandanten(models.Model):
    _name='res.partner'
    _inherit=['res.partner','mail.thread']
    #_inherits={'backend.mandanten':'backendmandant_id'}
    backendmandant_id=fields.Many2one('backend.mandanten', ondelete='cascade', index=True, auto_join=True)
 
    ist_mandant=fields.Boolean('Ist Mandant')
    contact_id=fields.Many2one('backend.kontakte', string='Contact ID')
    bank_rel=fields.One2many('bank.detail', 'mandant_id')
    order_id=fields.One2many('client.order', 'clientorder_id')
    number_id=fields.One2many('client.number', 'name')
    ticketing_rel=fields.One2many('project.issue','project_id')
    # branch_id=fields.One2many('backend.kanzleien','name')
   # partner_id=fields.Many2one('res.partner')
    
    #client_number=fields.Char(related="name.client_number" , string='Client Number')
    acc_id=fields.Many2one('bank.detail', string='Steuerberater')
    #branch_id=fields.Many2one('branch.branch', string='Branchs')
    issued_on=fields.Date('Ausgestellt am')
    
