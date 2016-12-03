# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_mandanten(models.Model):
    _name='backend.mandanten'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    name=fields.Char(String="Mandant", help="Name des Mandanten", required=True)
    bemerkung=fields.Text()
    mandantennummer=fields.Char('Mandantennummer',required=True, index=True) 
    emailpisa=fields.Char(String="eMailPISA")
    kanzlei=fields.Many2one('backend.kanzleien', ondelete='set null', String="Kanzlei", index=True)
    steuerberater=fields.Many2one('backend.berater', ondelete='set null', String="Steuerberater", index=True)
    unternehmensform=fields.Many2one('backend.unternehmensformen', ondelete='set null', String="Unternehmensform", index=True)
    branche=fields.Many2one('backend.branchen', ondelete='set null', String="Branche")
    status=fields.Many2one('backend.mandantenstatus', ondelete='set null', index=True)
    empfaenger1=fields.Char()
    empfaenger2=fields.Char()
    strasse=fields.Char('Straße')
    hausnummer=fields.Char()
    plz=fields.Char()
    ort=fields.Char()
    bundesland=fields.Char()
    land=fields.Char()
    adresse=fields.Char()
    bankname=fields.Char('Bank')
    bic=fields.Char('BIC')
    iban=fields.Char('IBAN')
    kontoinhaber=fields.Char('Kontoinhaber')
    telefon1=fields.Char('Telefon1')
    telefon2=fields.Char('Telefon2')
    email1=fields.Char('Email1')
    email2=fields.Char('Email2')
    datenok=fields.Boolean('Daten OK',default=False)
    
