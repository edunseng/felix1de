# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import methods

class backend_unternehmensformen(models.Model): #Companytype
    _name='backend.unternehmensformen'
    _inherit='backend.methods.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char("Unternehmensform")