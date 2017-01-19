# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import methods

class backend_paketkategorie(models.Model):
    _name='backend.paketkategorie'
    _inherit='backend.methods.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Kategorie")
    description=fields.Text('Beschreibung')