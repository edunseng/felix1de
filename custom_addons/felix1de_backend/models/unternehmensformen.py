# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_unternehmensformen(models.Model):
    _name='backend.unternehmensformen'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char("Unternehmensform")