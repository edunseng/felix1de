# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import methods

class backend_mandantenstatus(models.Model):
    _name='backend.mandantenstatus'
    _inherit='backend.methods.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char('Status')