# -*- coding: utf-8 -*-

#SALES.ORDER
from openerp import models, fields, api,_
import methods

class backend_abrechnungszeitraeume(models.Model):
    _name='backend.abrechnungszeitraeume'
    _rec_name = 'abr_accperiod'  # the default
    _order = 'abr_accperiod,id'
    _description = "Accounting Periods"
    _inherit=['backend.methods.accessid']   

    abr_accessid=fields.Char('ID', compute='_lookup_accessid')
    abr_accperiod=fields.Char('Abrechnungszeitraum') #Accounting Period
    abr_duedate=fields.Char("Fälligkeit")#Due Date               
    abr_description=fields.Text('Beschreibung')#Description