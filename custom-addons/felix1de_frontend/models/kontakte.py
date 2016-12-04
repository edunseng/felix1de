# -*- coding: utf-8 -*-
from openerp import models, fields, api,_

class BackendKontakte(models.Model):
    _name='backend.kontakte'
    _inherit=['backend.kontakte','mail.thread']
    
    #client_id=fields.One2many('backend.mandanten', 'contact_id')
    #ticket_id=fields.One2many('felix1.ticket', 'contact_id')
    #brach_contract=fields.Many2one('backend.kanzleien')
    image=fields.Binary(String="image")
    contact_id=fields.Char(string="Contact Id")
    remark=fields.Text('Remark')
    #category_id=fields.Many2one('res.partner.category',string='Tags')
    con_acquired_by=fields.Char('Acquired By')
    contact_since=fields.Char('Kontakt seit')
   # partner_id=fields.Many2one('res.partner')
    @api.model
    def _create_res_partner_from_kontact(self, vals):
	""" Create new Partner"""
	seq = {
              'name': vals['name'],
              'is_kontact':True,
            
		}
        
        return self.env['res.partner'].create(seq)    

    @api.model
    def create(self, vals):
	# We just need to create the relevant id 
       
	if not vals.get('partner_id'):
	   vals.update({'partner_id': self.sudo()._create_res_partner_from_kontact(vals).id}) 
         
	return super(BackendKontakte, self).create(vals)
