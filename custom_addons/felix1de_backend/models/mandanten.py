# -*- coding: utf-8 -*-
#RES.PARTNEr
from openerp import models, fields, api,_

class backend_mandanten(models.Model):
    _name='backend.mandanten'
    _rec_name = 'man_mandant'  # the default
    _order = 'man_mandant,id'
    _description = "Mandanten Main Model"     
    
    man_accessid=fields.Char('ID', compute='_lookup_accessid') #Access ID
    man_mandant=fields.Char(String="Mandant", help="Name des Mandanten", required=True)# Mane of Client(Mandanten)
    man_bemerkung=fields.Text()#remarks
    man_mandantennummer=fields.Char('Mandantennummer',required=True, index=True)#clientnumber 
    man_emailpisa=fields.Char(String="eMailPISA")#email PISA (special emailaddress)
    man_kanzlei=fields.Many2one('backend.kanzleien', ondelete='set null', String="Kanzlei", index=True)#Client's Company
    man_steuerberater=fields.Many2one('backend.berater', ondelete='set null', String="Steuerberater", index=True)#Client's Accountant
    man_unternehmensform=fields.Many2one('backend.unternehmensformen', ondelete='set null', String="Unternehmensform", index=True)#Client's Company Type
    man_branche=fields.Many2one('backend.branchen', ondelete='set null', String="Branche")#Client's Business Field
    man_status=fields.Many2one('backend.mandantenstatus', ondelete='set null', index=True)#Client's status
    man_empfaenger1=fields.Char('Empfaenger 1')#Client's Adress (Recipient 1)
    man_empfaenger2=fields.Char('Empfaenger 2')#Client's Adress (Recipient 2)
    man_strasse=fields.Char('Straße')#Client's Adress (Street)
    man_hausnummer=fields.Char('Hausnummer')#Client's Adress (Street number)
    man_plz=fields.Char('PLZ')#Client's Adress (ZIP)
    man_ort=fields.Char('Ort')#Client's Adress (City)
    man_bundesland=fields.Char('Bundesland')#Client's Adress (state)
    man_land=fields.Char('Land')#Client's Adress (country)
    man_adresse=fields.Char('Addresse')#Client's Adress (Address)
    man_bankname=fields.Char('Bankname')#Client's Bank (Bankname)
    man_bic=fields.Char('BIC')#Client's Bank (BIC)
    man_iban=fields.Char('IBAN')#Client's Bank (IBAN)
    man_kontoinhaber=fields.Char('Kontoinhaber')#Client's Bank (Account holder name)
    man_telefon1=fields.Char('Telefon1')#Client's Telefon1
    man_telefon2=fields.Char('Telefon2')#Client's Telefon2
    man_email1=fields.Char('Email1')#Client's Email1
    man_email2=fields.Char('Email2')#Client's Email2
    man_datenok=fields.Boolean('Daten OK',default=False)#Client's details OK
    
