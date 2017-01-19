# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

       
class backend_methods_accessid(models.Model):
    _name='backend.methods.accessid'
    
    @api.multi
    def _lookup_accessid(self):
        for record in self:
            record.accessid = str(record.id)

class backend_methods_autoname(models.Model):
    _name='backend.methods.autoname'

    @api.onchange('vorname','anrede','titel')
    def _auto_vornamename(self):
        self.vornamenachname =str (self.anrede)+" "+str(self.titel)+" "+ str(self.vorname) + " , " + str(self.nachname)
        self.nachnamevorname =str(self.nachname) + " , " + str(self.vorname)
    
            
   #@api.onchange('plz')
   # def _auto_adresse(self):
   #     self.addresse = str(self.strasse) + " " + str(self.hausnummer) + ", " + self.plz + " " + self.ort
   # 
   
   # @api.depends('vorname', 'nachname')
   # def _auto_namevorname(self):
   #     for record in self:
   #         record.name = str(record.nachname) + ", " + str(record.vorname)
   
   # @api.depends('vorname', 'nachname')
   # def _auto_vornamename(self):
   #     for record in self:
   #         record.name = str(record.vorname) + ", " + str(record.nachname)            
            
   
        # Can optionally return a warning and domains
        #return {
        #    'warning': {
        #        'title': "Something bad happened",
        #        'message': "It was very bad indeed",
        #            }
        #        }