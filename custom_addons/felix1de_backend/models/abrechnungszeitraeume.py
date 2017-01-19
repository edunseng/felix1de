# -*- coding: utf-8 -*-

#SALES.ORDER
from openerp import models, fields, api,_

class backend_abrechnungszeitraeume(models.Model):
    _name='backend.abrechnungszeitraeume'
    _rec_name = 'abr_accperiod'  # the default
    _order = 'abr_accperiod,id'
    _description = "Abrechnungszeitraeume"
   

    abr_accessid=fields.Char('ID', compute='_lookup_accessid') #MS Access ID
    abr_accperiod=fields.Char('Abrechnungszeitraum') #Accounting Period
    abr_duedate=fields.Char("Fälligkeit")#Due Date               
    abr_description=fields.Text('Beschreibung')#Description
    
    @api.multi
    def _lookup_accessid(self):
        for record in self:
            record.accessid = str(record.id)