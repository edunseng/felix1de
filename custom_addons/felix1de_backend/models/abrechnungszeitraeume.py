# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_abrechnungszeitraeume(models.Model):
    _name='backend.abrechnungszeitraeume'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Abrechnungszeitraum")
    faelligkeit=fields.Char("Fälligkeit")
    beschreibung=fields.Text('Beschreibung')