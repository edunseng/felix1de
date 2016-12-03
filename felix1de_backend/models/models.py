# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

#Access Backend 
class felix1_backend(models.Model):
    _name='felix1de.backend'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Backend Version", help="Access Backend Version", readonly=True)
    description=fields.Text()

#Acces Tabellen

#AAA_Jahresplan
#class aaa_jahresplan(models.Model):
    
# class felix1de_backend(models.Model):
#     _name = 'felix1de_backend.felix1de_backend'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100