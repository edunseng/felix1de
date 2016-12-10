# -*- coding: utf-8 -*-
from openerp import models, fields, api,_

class BackendKanzleien(models.Model):
    _name='backend.kanzleien'
    _inherit=['backend.kanzleien','mail.thread']
    
    #branch=fields.Many2one('backend.mandanten')
    #brach_contract_rel=fields.One2many('backend.kontakte','brach_contract')
    #contact_person_id=fields.One2many('backend.kontakte','brach_contract')
    branch_phone=fields.Char('branch phone')
    address=fields.Char('Address')
    branch_street=fields.Char('branch_street')
    branch_street_no=fields.Char('branch_street_no')
    branch_house_no=fields.Char('branch_house_no')
    branch_street_extra=fields.Char('branch_street_extra')
    branch_city=fields.Char('branch_city')
    branch_post_code=fields.Char('branch_post_code')
    branch_mail=fields.Char('branch_mail')
    branch_city_extra=fields.Char('branch_city_extra')
    #branch_country=fields.Many2one('res.country')
    #branch_state=fields.Many2one('res.country.state')
    #company_id=fields.Many2one('res.company')
    #partner_id=fields.Many2one('res.partner')
    #@api.model
    #def _create_res_compnay_from_branch(self, vals):
	#""" Create new project task"""
	#seq = {
        #      'name': vals['name'],
        #      'email':vals['email'],
        #      'phone': vals['branch_phone'],
        #      'street':vals['branch_street'],
        #      'street2':vals['branch_street_extra'],
        #      'city':vals['branch_city'],
        #      'zip':vals['branch_post_code'],
        #      'country_id':vals['branch_country'],
        #      'state_id':vals['branch_state'],
        #      'partner_id':vals['partner_id']
	#	}
        
        #return self.env['res.company'].create(seq)    

   # @api.model
   # def create(self, vals):
	# We just need to create the relevant id 
        #projct_lst=[]
	#if not vals.get('company_id'):
	#   vals.update({'company_id': self.sudo()._create_res_compnay_from_branch(vals).id}) 
         
	#return super(BackendKanzleien, self).create(vals)
    
    
