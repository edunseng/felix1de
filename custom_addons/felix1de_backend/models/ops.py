# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import methods

class backend_ops(models.Model):
    _name='backend.ops'
    _inherit='backend.methods.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    opid=fields.Char('OpID')
    name=fields.Char('OpName')
    opinhaber=fields.Char('OpInhaber')
    accountname=fields.Char('AccountName')
    erstelldatum=fields.Date('Erstelldatum')
    schlusstermin=fields.Date('Schlusstermin')
    phasendauer=fields.Integer('Phasendauer')
    kampagne=fields.Char('Kampagne')
    leadquelle=fields.Char('LeadQuelle')
    status=fields.Char('Status')
    wert=fields.Monetary('Wert')
    branche=fields.Char('Branche')
    mandantennr=fields.Char('MandantenNr')
    beschreibung=fields.Text('Beschreibung')
    currency_id=fields.Many2one('res.currency',string='Währung')