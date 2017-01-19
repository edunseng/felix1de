# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_checklistentypen(models.Model):
    _name='backend.checklistentypen'
    _rec_name = 'chetyp_bezeichnung'  # the default
    _order = 'chetyp_bezeichnung,id'
    _description = "Checklisten Typen Main Model" 
    
    chetyp_accessid=fields.Char('ID', compute='_lookup_accessid')
    
    chetyp_bezeichnung=fields.Char('Bezeichnung')
    chetyp_description=fields.Text('Beschreibung')
    
    
    @api.multi
    def _lookup_accessid(self):
        for record in self:
            record.accessid = str(record.id)