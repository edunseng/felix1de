# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import methods

class backend_checklistenvorlagen(models.Model):
    _name='backend.checklistenvorlagen'
    _inherit='backend.methods.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Bezeichnung")
    typ=fields.Many2one("backend.checklistentypen", string="Typ", ondelete='set null')
    beschreibung=fields.Text('Beschreibung')
    
    