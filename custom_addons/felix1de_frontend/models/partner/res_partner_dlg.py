# -*- coding: utf-8 -*-
from openerp import models, fields, api,_

class resPartnerKontakte(models.Model):
    _name='res.partner'
    _inherit=['res.partner','mail.thread']
   # _inherits={'backend.kontakte':'backendkontakt_id'}
    backendkontakt_id=fields.Many2one('backend.kontakte', ondelete='cascade', index=True, auto_join=True)
    
#        _inherit='res.partner' 

    
    ist_kontakt=fields.Boolean('Ist Kontakt')
    #client_id=fields.One2many('backend.mandanten', 'contact_id')
    #ticket_id=fields.One2many('felix1.ticket', 'contact_id')
    #brach_contract=fields.Many2one('backend.kanzleien')
    ##image=fields.Binary(String="image")
   ## contact_id=fields.Char(string="Contact Id")
    remark=fields.Text('Bemerkung')
    #category_id=fields.Many2one('res.partner.category',string='Tags')
   
   ## contact_since=fields.Char('Kontakt seit')


    ist_kontakt=fields.Boolean('Ist Kontakt')
    image=fields.Binary(String="Bild")
    #name=fields.Char('Name des Mandanten', invisible=True)
    last_name=fields.Char('Nachname')
    contact_id=fields.Char('Kontakt ID')
    con_acquired_by=fields.Char('vermittelt durch')
    contact_since=fields.Char('Kontakt seit')
    phone=fields.Char('Telefon')
    mobile=fields.Char('Handy')
    fax=fields.Char('Fax')
    email=fields.Char('email')
    comment=fields.Char('Bemerkung')
    title=fields.Char('Titel')
    house_no=fields.Char('Hausnummer')
    street=fields.Char('Strasse')
    street2=fields.Char('Strase2')
    zip=fields.Char('PLZ')
    city=fields.Char('Stadt')
    state=fields.Char('Bundesland')
    kontakt_seit=fields.Date('Kontakt Seit')
    country_id=fields.Many2one('res.country')
    ticket_id=fields.One2many('felix1.ticket', 'contact_id')
    client_id=fields.One2many('res.partner', 'contact_id')
    
    
        
    @api.onchange('name','mobile')
    def _auto_name(self):
        self.nachname=self.name
        self.telefon2=self.mobile
        #....
        