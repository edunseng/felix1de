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
    remark=fields.Text('Remark')
    #category_id=fields.Many2one('res.partner.category',string='Tags')
   
   ## contact_since=fields.Char('Kontakt seit')


    
    image=fields.Binary(String="image")
    #name=fields.Char('Name des Mandanten', invisible=True)
    last_name=fields.Char('last name')
    contact_id=fields.Char('Contact ID')
    con_acquired_by=fields.Char('Acquired By')
    contact_since=fields.Char('Kontakt seit')
    phone=fields.Char('phone')
    mobile=fields.Char('mobile')
    fax=fields.Char('fax')
    email=fields.Char('email')
    comment=fields.Char('comment')
    title=fields.Char('title')
    house_no=fields.Char('house_no')
    street=fields.Char('street')
    street2=fields.Char('street2')
    zip=fields.Char('zip')
    city=fields.Char('city')
    state=fields.Char('state')
    kontakt_seit=fields.Date('Kontakt Seit')
    country_id=fields.Many2one('res.country')
    ticket_id=fields.One2many('felix1.ticket', 'contact_id')
    client_id=fields.One2many('res.partner', 'contact_id')
    
    
        
    @api.onchange('name','mobile')
    def _auto_name(self):
        self.nachname=self.name
        self.telefon2=self.mobile
        #....
        