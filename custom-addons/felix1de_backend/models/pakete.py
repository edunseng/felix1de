# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais
 
class backend_pakete(models.Model):
    _name='backend.pakete'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Many2one("backend.paket", string="Paket", index=True)
    kategorie=fields.Many2one("backend.paketkategorie", string="Packetkathegorie")
    beschreibung=fields.Text("Beschreibung" )
    produktbild=fields.Binary("Produktbild")
    leistungserbringer=fields.Char('Leistungserbringer')#Many2one("backend.felix1gruppen", string="Leistungserbringer") 
    unternehmensformen=fields.Char('Unternehmensform')#One2many("backend.unternehmensformen","name", string="Unternehmensformen")#
    derivatvon=fields.Many2one("backend.paket", string="DerivatVon", index=True)
    preisab=fields.Char("PreisAb")
    bruttopreis=fields.Boolean("Bruttopreis", default=False)
    standardgebuehr=fields.Monetary("Standardgebühr")
    abrechnungszeitraum=fields.Many2one("backend.abrechnungszeitraeume", string="Abrechnungszeitraum", index=True)
    produktseite=fields.Text("Produktseite")
    bestellLink=fields.Text("Bestell-Link")
    checkliste=fields.Many2one('backend.checklistenvorlagen', string="Checkliste")
    rechnungstext=fields.Char("Rechnungstext")
    ident=fields.Boolean("Ident", default=False)
    vollmacht=fields.Boolean("Vollmacht", default=False)
    pisa=fields.Boolean("PISA", default=False)
    sageone=fields.Boolean("SageOne", default=False)
    app=fields.Boolean("App", default=False)
    besonderheiten=fields.Text("Besonderheiten")
    status=fields.Many2one('backend.paketestatus', string="Paketestatus", index=True)#
    mandantengruppe=fields.Integer("Mandantengruppe", default="0")
    websiteid=fields.Integer("WebsiteID")
    preisschluessel=fields.Many2one('backend.preiseschluessel', string="Preisschluessel", index=True)#
    datenok=fields.Boolean("DatenOK", default=False)
    currency_id=fields.Many2one('res.currency', string='Währung')
    
