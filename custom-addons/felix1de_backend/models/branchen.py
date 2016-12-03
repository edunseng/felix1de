# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import apiais

class backend_branchen(models.Model):
    _name='backend.branchen'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char('Branche')
    kategorie=fields.Selection(String='Kategorien', selection=[('Dienstleistung', 'Dienstleistung'),
                                                          ('Einzelhandel','Einzelhandel'),
                                                          ('Handwerker','Handwerker'),
                                                          ('Heilberufe und Betreuung', 'Heilberufe und Betreuung'),
                                                          ('Hotels und Gaststätten','Hotels und Gaststätten'),
                                                          ('Immobilien', 'Immobilien'),
                                                          ('Kfz', 'Kfz'),
                                                          ('Sonstige', 'Sonstige')])