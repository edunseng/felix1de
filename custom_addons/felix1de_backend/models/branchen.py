# -*- coding: utf-8 -*-
#RES.COMPANY
from openerp import models, fields, api,_

class backend_branchen(models.Model):
    _name='backend.branchen'
    _rec_name = 'bra_branche'  # the default
    _order = 'bra_branche,id'
    _description = "Branche Main Model"  
    
    bra_accessid=fields.Char('ID', compute='_lookup_accessid')
    
    bra_branche=fields.Char(string="Branche")
    bra_kategorie=fields.Selection(String='Kategorien', selection=[('Dienstleistung', 'Dienstleistung'),
                                                          ('Einzelhandel','Einzelhandel'),
                                                          ('Handwerker','Handwerker'),
                                                          ('Heilberufe und Betreuung', 'Heilberufe und Betreuung'),
                                                          ('Hotels und Gaststätten','Hotels und Gaststätten'),
                                                          ('Immobilien', 'Immobilien'),
                                                          ('Kfz', 'Kfz'),
                                                          ('Sonstige', 'Sonstige')],string="Kathegorie")
    
    @api.multi
    def _lookup_accessid(self):
        for record in self:
            record.accessid = str(record.id)