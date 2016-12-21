from openerp import fields,models,api,_
class res_partner(models.Model):
   _inherit='res.partner'
   lastname=fields.Char()
   client_value=fields.Char('Mandant',)
   client_number=fields.Char('Mandantennr.')
   client_number_spcl=fields.Char('Lohn-Mandantennr.')
   client_since=fields.Date('Mandant seit')
   acquired_by=fields.Char('Gewonnen durch')
   bank_id=fields.Many2one('bank.detail')
   bank_rel=fields.One2many('bank.detail', 'client_id')
   branch_rel=fields.Many2one('branch.branch')
   partner_rel_id=fields.Many2many('res.partner' ,'res_id', 'res_idss')
   order_id=fields.One2many('client.order', 'name')
   number_id=fields.One2many('client.number', 'name')
   con_acquired_by=fields.Char('Gewonnen Durch')
   contact_since=fields.Char('Kontakt seit')
   lagel_structure=fields.Char('Rechtsform')
   client_id=fields.Char('Mandant ID')
   contact_id=fields.Char('Kontakt ID')
   client_remark=fields.Text('Bemerkung')
   client_status=fields.Char('Status')
   house_no=fields.Char()
   consultant_id=fields.Char('Bearbeiter ID')
   etl_user_identification=fields.Char('Name ETL Stammkanzlei')
   house_contact_person=fields.Char('Ansprechpartner')
   client_issue_date=fields.Date('Ausstellungdatum')
   client_detail_id=fields.One2many('res.client', 'partner_id')
   branch_id=fields.One2many('branch.branch','contract_person')
   type_ext= fields.Selection(
            [
             ('invoice', 'Rechnungsanschrift'),
             ('delivery', 'Lieferanschrift'),
             ('other', 'alternative Anschrift')], 'Address Type', default='invoice',
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
		       }
	
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
   client_number=fields.Char(related='client_id.client_number')
   account_number=fields.Char('Kontonummer')
   iban=fields.Char('IBAN')
   bic=fields.Char('BIC')
   Payment_method=fields.Char('Zahlungsart')
   valid_from=fields.Date('Gueltig ab')
class client_number(models.Model):
   _name="client.number"
   name=fields.Char('Name')
   client_id=fields.Many2one('res.partner', 'Mandant')
   branch_id=fields.Many2one('branch.brach', 'Branche')
   bank_id=fields.Many2one('bank.detail', 'Steuerberater')
   lohn_agent_no=fields.Char('Lohn-Mandantennr.')

class client_detail(models.Model):
	_name='res.client'
	name=fields.Many2one('res.partner', string="Name")
	partner_id=fields.Many2one('res.partner')
	client_number=fields.Char(related="name.client_number" , string='Mandantennr.')
	account_id=fields.Many2one('bank.detail', string='Steuerberater')
	branch_id=fields.Many2one('branch.branch', string='Branche')
	issue_date=fields.Date('Ausgestellet Am')
	
