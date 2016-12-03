# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_preiseschluessel(models.Model):
    _name='backend.preiseschluessel'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    beschreibung=fields.Text('Beschreibung')
    name=fields.Char('Schlüssel')
    abrechnungszeitraum=fields.Many2one('backend.abrechnungszeitraeume', string='Abrechnungszeitraum')#
    istbruttopreis=fields.Boolean('IstBruttopreis', default=False)
    mehrfachbuchbar=fields.Boolean('MehrfachBuchbar', help="gilt z.B. für Lohnabrechnung", default=False)
    provision=fields.Monetary('Provision')
    currency_id=fields.Many2one('res.currency', string="Währung")
    