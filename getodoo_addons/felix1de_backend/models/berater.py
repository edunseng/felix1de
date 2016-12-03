# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais


class backend_berater(models.Model):
    _name='backend.berater'
    _inherit='backend.apiais.autoname','backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    nachname=fields.Char('Nachname', help="Name des Steuerberaters", required=True)
    bemerkung=fields.Text('Bemerkung')
    beraterid=fields.Char('Berater ID')
    etlbenutzername=fields.Char('ETL Benutzername')
    vorname=fields.Char('Vorname', help="Vorname des Steuerberaters", required=False)
    anrede=fields.Selection([(u"\u0020", 'kein'),('Herr', 'Herr'),('Frau', 'Frau')],default=u"\u0020")
    titel=fields.Selection(String="Titel", selection=[(u"\u0020", 'kein'),('Dr.', 'Dr.'),('Prof.','Prof.'),('Prof. Dr.','Prof. Dr.')],default= u"\u0020")
    kanzleileiter=fields.Boolean('Kanzleileiter', dafault=False)
    ansprechpartner=fields.Boolean('Ansprechpartner',default=False)
    stb=fields.Boolean('StB', help="Steuerberater",default=False)
    stbIn=fields.Boolean('StBIn', help="SteuerberaterIn", default=False)
    ra=fields.Boolean('RA',help="Rechtsanwalt", default=False)
    wp=fields.Boolean('WP', help="??", default=False)
    weiteretitel=fields.Char('Weitere Titel')
    hochschulabschluss=fields.Char('Hochschulabschluss')
    foto=fields.Binary('Foto')
    vornamenachname=fields.Char('Vorname, Nachname')
    name=fields.Char('Nachname, Vorname')
    telefon1=fields.Char('Telefon1')
    telefon2=fields.Char('Telefon2')
    telefon3=fields.Char('Telefon3')
    email1=fields.Char('Email1')
    email2=fields.Char('Email2')
    email3=fields.Char('Email3')
    fax=fields.Char('Fax')
    datenok=fields.Boolean('Daten OK',default=False)
    
    

    

    