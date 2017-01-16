# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import methods

class backend_paket(models.Model):
    _name='backend.paket'
    _inherit='backend.methods.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Paket")
    description=fields.Text('Beschreibung')