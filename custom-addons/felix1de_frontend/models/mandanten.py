# -*- coding: utf-8 -*-
from openerp import models, fields, api,_

class BackendMandanten(models.Model):
    _name='backend.mandanten'
    _inherit=['backend.mandanten','mail.thread']
 
    #contact_id=fields.Many2one('backend.kontakte', string='Contact ID')
   # bank_rel=fields.One2many('bank.detail', 'mandant_id')
   # order_id=fields.One2many('client.order', 'client_order_id')
    #number_id=fields.One2many('client.number', 'name')
    #ticketing_rel=fields.One2many('felix1.ticket','priPriority_id')
    #branch_id=fields.One2many('backend.kanzleien','branch')
   # partner_id=fields.Many2one('res.partner')
    image=fields.Binary(String="image")
    @api.model
    def _create_res_partner_from_mandant(self, vals):
	""" Create new Partner"""
	seq = {
              'name': vals['name'],
              'is_mandant':True,
            
		}
        
        return self.env['res.partner'].create(seq)    

    @api.model
    def create(self, vals):
	# We just need to create the relevant id 
       
	if not vals.get('partner_id'):
	   vals.update({'partner_id': self.sudo()._create_res_partner_from_mandant(vals).id}) 
         
	return super(BackendMandanten, self).create(vals)
    
