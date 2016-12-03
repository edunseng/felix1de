# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_lohnmandanten(models.Model):
    _name='backend.lohnmandanten'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char('Mandantennummer')
    edlohnBeraternummer=fields.Char('edlohnBeraternummer')
    edlohnmandantennummer=fields.Char('edlohnMandantennummer')
    Zahlungsweise=fields.Char('Zahlungsweise')
    abweichenderAbrechnungsmonat=fields.Char('abweichenderAbrechnungsmonat')
    Zusatzprodukt=fields.Integer('Zusatzprodukt')
    GlaubigerID=fields.Char('GlaubigerID')
    Debitorennummeredfibu=fields.Char('Debitorennummeredfibu')
    beschreibung=fields.Text('Beschreibung')
    