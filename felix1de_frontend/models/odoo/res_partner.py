# -*- coding: utf-8 -*-
from openerp import fields,models,api,_

class res_partner(models.Model):
   _inherit=['backend.mandanten','backend.kontakte']
   _inherit='res.partner'
   
   lastname=fields.Char()
   client_value=fields.Boolean('Client',)
   client_number=fields.Char('Clientnumber')
   client_number_spcl=fields.Char()
   client_since=fields.Date('Client Since')
   acquired_by=fields.Char('Acquired By')
   bank_id=fields.Many2one('bank.detail')
   bank_rel=fields.One2many('bank.detail', 'client_id')
   branch_rel=fields.Many2one('branch.branch')
   partner_rel_id=fields.Many2many('res.partner' ,'res_id', 'res_idss')
   order_id=fields.One2many('client.order', 'name')
   number_id=fields.One2many('client.number', 'name')
   con_acquired_by=fields.Char('Acquired By')
   contact_since=fields.Char('Contact Since')
   lagel_structure=fields.Char('Legal Structure')
   client_id=fields.Char('Client ID')
   contact_id=fields.Many2one('contact.contacts', string='Contact ID')
   client_remark=fields.Text('Remark')
   client_status=fields.Char('Status')
   house_no=fields.Char()
   consultant_id=fields.Char('Consltant ID')
   etl_user_identification=fields.Char()
   house_contact_person=fields.Char('House Contact Person Chamber')
   client_issue_date=fields.Date('Issue Date')
   client_detail_id=fields.One2many('res.client', 'partner_id')
   branch_id=fields.One2many('branch.branch','contract_person')
   type_ext= fields.Selection(
            [
             ('invoice', 'Invoice address'),
             ('delivery', 'Shipping address'),
             ('other', 'Other address')], 'Address Type', default='invoice',
            help="Used to select automatically the right address according to the context in sales and purchases documents.")
   @api.multi
   def client_list_view(self):
       for record in self:
           for  rec in record.client_detail_id:
	       return {
		      'name': _('Client Lists'),
		       'view_type': 'form',
			'view_mode': 'tree,form',
			'res_model': 'res.client',
			'view_id': False,
			'type': 'ir.actions.act_window',
			'domain': [('id', 'in', [rec.id for rec in record.client_detail_id])],
		       }         #res.partner    #rec.client          #res.partner
	
   @api.multi
   @api.onchange('type_ext')
   def type_value(self):
       for record in self:
           if record.type_ext == 'invoice':
              record.type='invoice'
           if record.type_ext == 'delivery':
              record.type='delivery'
           if record.type_ext == 'other':
              record.type='other'
  
class res_bank_detial(models.Model):
   _name='bank.detail'
   name=fields.Char()
   client_id=fields.Many2one('res.partner')
   mandant_id=fields.Many2one('backend.mandanten')
   client_number=fields.Char(related='client_id.client_number')
   account_number=fields.Char('Account Number')
   iban=fields.Char('IBAN')
   bic=fields.Char('BIC')
   Payment_method=fields.Char('Payment Method')
   valid_from=fields.Date('Valid From')
class client_number(models.Model):
   _name="client.number"
   name=fields.Many2one('backend.mandanten')
   client_id=fields.Many2one('res.partner', 'Client')
   branch_id=fields.Many2one('branch.brach', 'Branch')
   bank_id=fields.Many2one('bank.detail', 'Accountant')
   lohn_agent_no=fields.Char('Lohn AgentNumber')

class client_detail(models.Model):
	_name='res.client'
	name=fields.Many2one('res.partner', string="Name")
	partner_id=fields.Many2one('res.partner')
	client_number=fields.Char(related="name.client_number" , string='Client Number')
	account_id=fields.Many2one('bank.detail', string='Accountant')
	branch_id=fields.Many2one('branch.branch', string='Branchs')
	issue_date=fields.Date('Issued On')
	
