# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_paket(models.Model):
    _name='backend.paket'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Paket")
    description=fields.Text('Beschreibung')