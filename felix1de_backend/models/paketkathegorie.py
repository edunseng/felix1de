# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_paketkategorie(models.Model):
    _name='backend.paketkategorie'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Kategorie")
    description=fields.Text('Beschreibung')