# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_paketestatus(models.Model):
    _name='backend.paketestatus'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Paketestatus")
    description=fields.Text('Beschreibung')