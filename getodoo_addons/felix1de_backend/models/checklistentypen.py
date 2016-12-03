# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_checklistentypen(models.Model):
    _name='backend.checklistentypen'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Bezeichnung")
    description=fields.Text('Beschreibung')