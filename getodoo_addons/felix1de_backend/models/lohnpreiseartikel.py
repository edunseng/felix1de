# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais
 
class backend_lohnpreiseartikel(models.Model):
    _name='backend.lohnpreiseartikel'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    produktkategorie=fields.Integer("Produktkategorie")
    preiseschluesselschluessel=fields.Integer('PreiseSchluesselSchluessel')
    artikellohnnummer=fields.Char('ArtikelLohnNummer')
    preis=fields.Monetary('Preis')
    name=fields.Char('ArtikelLohnName')
    etlnrpkc=fields.Integer('ETLNrPKC')
    erloeskonto=fields.Char('Erloeskonto')
    zahlungsweise=fields.Char('Zahlungsweise')
    beschreibung=fields.Char('Beschreibung')
    currency_id=fields.Many2one('res.currency',string='Währung')
    
    
