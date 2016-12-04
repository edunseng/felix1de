# -*- coding: utf-8 -*-
from openerp import models, fields, api,_

class BackendKontakte(models.Model):
    _name='res.partner'
    _inherit=['res.partner','mail.thread']
    
    is_kontakt=fields.Boolean('Ist Kontakt')
    #client_id=fields.One2many('backend.mandanten', 'contact_id')
    #ticket_id=fields.One2many('felix1.ticket', 'contact_id')
    #brach_contract=fields.Many2one('backend.kanzleien')
    ##image=fields.Binary(String="image")
   ## contact_id=fields.Char(string="Contact Id")
    ##remark=fields.Text('Remark')
    #category_id=fields.Many2one('res.partner.category',string='Tags')
   ## con_acquired_by=fields.Char('Acquired By')
   ## contact_since=fields.Char('Kontakt seit')
    backkontakt_id=fields.Many2one('backend.kontakte')
    @api.model
    def _create_res_partner_from_kontact(self, vals):
	""" Create new Partner"""
    
	seq = {
              'nachname': vals['name'],
              'vorname': vals['vorname'],
              'is_kontakt':True,
            
		}
        
        return self.env['backend.kontakte'].create(seq)    

    @api.model
    def create(self, vals):
	# We just need to create the relevant id 
       
	if not vals.get('backkontakt_id'):
	   vals.update({'backkontakt_id': self.sudo()._create_res_partner_from_kontact(vals).id}) 
         
	return super(BackendKontakte, self).create(vals)
