# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import methods

class backend_mapping_kontakte_mandanten(models.Model):
    _name='backend.mapping.kontakte.mandanten'
    _inherit='backend.methods.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    kontakt=fields.Many2one('backend.kontakte', string='Kontakte',domain='ist_kontak')#
    mandant=fields.Many2one('backend.mandanten', string='Mandanten')#domain 
    funktion=fields.Char('Funktion')
   # contanct??rel ) fields.Manz2manz*(|res.partner|,|contact?mandantant?rel|,|mandantant|,contanct?id,||Relation)
    #                                     model 1     postgre_tablename     field(model1) field(model2)-kontakt            