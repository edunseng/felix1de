# -*- coding: utf-8 -*-
from openerp import fields,models,api,_
class res_partner(models.Model):
    _inherit='res.partner'
    _rec_name='complete_name'
    
    lastname=fields.Char()
    complete_name = fields.Char('Complete Name')
    client_value=fields.Boolean('Client',)
    client_number=fields.Char('Mandantennummer')
    client_number_spcl=fields.Char('Lohnmandanten Nummer')
    client_since=fields.Date('Mandant Seit')
    acquired_by=fields.Char('vermittelt durch')
    bank_id=fields.Many2one('bank.detail')
   #bank_rel=fields.One2many('bank.detail', 'client_id')
    branch_rel=fields.Many2one('branch.branch', string='Niederlassung')
   #partner_rel_id=fields.Many2many('res.partner' ,'res_id', 'res_idss')
   #order_id=fields.One2many('client.order', 'name')
  #  number_id=fields.One2many('client.number', 'name')
    con_acquired_by=fields.Char('vermittelt durch')
    lagel_structure=fields.Char('rechtsform')
    clients_id=fields.Char('Mandantennummer')
   #contact_id=fields.Many2one('contact.contacts', string='Contact ID')
    client_remark=fields.Text('Bermerkung')
    client_status=fields.Char('Status')
    house_no=fields.Char('Hausnummer')
    consultant_id=fields.Char('Steuerberter ID')
    etl_user_identification=fields.Char('ETL-Identifikations Nummer')
    house_contact_person=fields.Char('Ansprechperson')
    client_issue_date=fields.Date('Ausstellungsdatum')
    client_detail_id=fields.One2many('res.client', 'partner_id')
    branch_id=fields.One2many('branch.branch','contract_person')
    tikmarkopen=fields.Boolean('vormerken')
    client_id=fields.One2many('res.partner','name',string='zugehoeriger Partner')
    niederlassung_id=fields.Many2one('branch.branch','Niederlassung')
   
    type_ext= fields.Selection(
            [
             ('invoice', 'Rechnungsanschrift'),
             ('delivery', 'Lieferanschrift'),
             ('other', 'Weitere Adressen')], 'Address Type', default='invoice',
            help="Je nach Kontext entsprechende Lieferdetails wählen.")
   
    bemerkung = fields.Char('Bemerkung')
    branche = fields.Char('Branche')
    bundesland = fields.Char('Bundesland')
    datenok = fields.Char('DatenOK')
    empfaenger1 = fields.Char('Empfaenger1')
    empfaenger2 = fields.Char('Empfaenger2')
    hausnummer = fields.Char('Hausnummer')
    record_id = fields.Integer('ID')
    kanzlei = fields.Char('Kanzlei')
    land = fields.Char('Land')
    ort = fields.Char('Ort')
    plz = fields.Char('PLZ')
    status = fields.Char('Status')
    steuerberater = fields.Char('Steuerberater')
    strasse = fields.Char('Strasse')
    telefon1 = fields.Char('Telefon1')
    telefon2 = fields.Char('Telefon2')
    unternehmensform = fields.Char('Unternehmensform')
    eMail1 = fields.Char('eMail1')
    eMail2 = fields.Char('eMail2')
    mandantennummer = fields.Char('Mandantennummer')
    
   
   
   
   
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
    
    
    @api.one
    def do_toggle_mode(self):
        self.tikmarkopen = not self.tikmarkopen
        return True
  
class res_bank_detial(models.Model):
   _name='bank.detail'
   
   name=fields.Char()
   client_id=fields.Many2one('res.partner')
   mandant_id=fields.Many2one('backend.mandanten')
   client_number=fields.Char(related='client_id.client_number')
   account_number=fields.Char('Kontonummerr')
   iban=fields.Char('IBAN')
   bic=fields.Char('BIC')
   Payment_method=fields.Char('Zahlungsmethode')
   valid_from=fields.Date('Gueltig von')
   
class client_number(models.Model):
   _name="client.number"

   name=fields.Many2one('backend.mandanten')
  # #client_id=fields.Many2one('res.partner', 'Client')
   branch_id=fields.Many2one('branch.branch', 'Niederlassung')
  # #bank_id=fields.Many2one('bank.detail', 'Steuerberater')
   lohn_agent_no=fields.Char('Lohn Agentnummer')

class client_detail(models.Model):
    _name='res.client'
    
    name=fields.Many2one('res.partner', string="Name")
    partner_id=fields.Many2one('res.partner')
    client_number=fields.Char(related="name.client_number" , string='Mandantennumber')
    acc_id=fields.Many2one('bank.detail', string='Steuerberater')
    branch_id=fields.Many2one('branch.branch', string='Niederlassung')
    issued_on=fields.Date('Ausgestellt am')
    
