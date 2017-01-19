# -*- coding: utf-8 -*-

from openerp import models, fields, api,_


class backend_checklistenvorlagen(models.Model):
    _name='backend.checklistenvorlagen'
    _rec_name = 'chevor_bezeichnung'  # the default
    _order = 'chevor_bezeichnung,id'
    _description = "Checklisten Vorlagen Main Model" 
    
    chevor_accessid=fields.Char('ID', compute='_lookup_accessid')
    
    chevor_bezeichnung=fields.Char('Bezeichnung')
    chevor_typ_id=fields.Many2one("backend.checklistentypen", string="Typ", ondelete='set null')
    chevor_beschreibung=fields.Text('Beschreibung')
    
    @api.multi
    def _lookup_accessid(self):
        for record in self:
            record.accessid = str(record.id)