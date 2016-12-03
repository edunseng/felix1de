# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_mandantenstatus(models.Model):
    _name='backend.mandantenstatus'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char('Status')