# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_kontakte(models.Model):
    _name='backend.kontakte'
    _inherit='backend.apiais.autoname','backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    vorname=fields.Char("Vorname")
    nachname=fields.Char("Nachname")
    anrede=fields.Selection(String="Anrede",selection=[(u"\u0020", 'kein'),('Herr', 'Herr'),('Frau','Frau')],default=u"\u0020")
    titel=fields.Selection(String="Titel", selection=[(u"\u0020", 'kein'),('Dr.', 'Dr.'),('Prof.','Prof.'),('Prof. Dr.','Prof. Dr.')],default=u"\u0020")
    name=fields.Char('Nachname, Vorname')
    vornamenachname=fields.Char('Vorname, Nachname')
    telefon1=fields.Char("Telefon1")
    telefon2=fields.Char("Telefon2")
    telefon3=fields.Char("Telefon3")
    email1=fields.Char("eMail1")
    email2=fields.Char("eMail2")
    email3=fields.Char("eMail3")
    fax=fields.Char("Fax")
    bemerkung=fields.Char("Bemerkung")
    vip=fields.Boolean("VIP", default=False)
    strasse=fields.Char("Strasse")
    hausnummer=fields.Char("Hausnummer")
    plz=fields.Char("PLZ")
    ort=fields.Char("Ort")
    bundesland=fields.Selection(String="Bundesland", selection=[('bw', 'Baden-Württemberg'),
                                            ('Bayern','Bayern'),
                                            ('Berlin','Berlin'),
                                            ('Brandenburg', 'Brandenburg'),
                                            ('Bremen', 'Bremen'),
                                            ('Hamburg', 'Hamburg'),
                                            ('Hessen', 'Hessen'),
                                            ('Mecklrnburg-Vorpommern', 'Mecklenburg-Vorpommern'),
                                            ('Niedersachsen', 'Niedersachsen'),
                                            ('Nordrhein-Westfalen', 'Nordrhein-Westfalen'),
                                            ('Rheinland-Pfalz', 'Rheinland-Pfalz'),
                                            ('Saarland', 'Saarland'),
                                            ('Sachsen', 'Sachsen'),
                                            ('Sachsen-Anhalt', 'Sachsen-Anhalt'),
                                            ('Schleswig-Holstein', 'Schleswig-Holstein'),
                                            ('Thüringen', 'Thüringen')])
    land=fields.Char("Land")
    addresse=fields.Char('Adresse')
    datenok=fields.Boolean("DatenOK", default=False)
     