# -*- coding: utf-8 -*-

from openerp import models, fields, api,_

class backend_kontakte(models.Model):
    _name='backend.kontakte'
    _rec_name = 'kon_vorname'  # the default
    _order = 'kon_vorname,id'
    _description = "Kontakte Main Model" 

    

    kon_accessid=fields.Char('ID', compute='_lookup_accessid')
    
    kon_vorname=fields.Char("Vorname")#Client's first name (Kontakte)
    kon_nachname=fields.Char("Nachname")#Client's Lastname
    kon_anrede=fields.Selection(String="Anrede",selection=[(u"\u0020", 'kein'),('Herr', 'Herr'),('Frau','Frau')],default=u"\u0020")#Client's title (mr. mrs. ..) 
    kon_titel=fields.Selection(String="Titel", selection=[(u"\u0020", 'kein'),('Dr.', 'Dr.'),('Prof.','Prof.'),('Prof. Dr.','Prof. Dr.')],default=u"\u0020")#Client's title (doctor, PhD,..)
    kon_nachnamevorname=fields.Char('Nachname, Vorname')#Client's firstname&lastname
    kon_vornamenachname=fields.Char('Vorname, Nachname')#Client's lastname&firstname
    kon_telefon1=fields.Char("Telefon1")#Client's telefon 1
    kon_telefon2=fields.Char("Telefon2")#Client's telefon 2
    kon_telefon3=fields.Char("Telefon3")#Client's telefon 3
    kon_email1=fields.Char("eMail1")#Client's email 1
    kon_email2=fields.Char("eMail2")#Client's email 2
    kon_email3=fields.Char("eMail3")#Client's email 3
    kon_fax=fields.Char("Fax")#Client's fax
    kon_bemerkung=fields.Char("Bemerkung")#Client's remark
    kon_vip=fields.Boolean("VIP", default=False)#Client is VIP?
    kon_strasse=fields.Char("Strasse")#Client's Address (street)
    kon_hausnummer=fields.Char("Hausnummer")#Client's Address (housenumber)
    kon_plz=fields.Char("PLZ")#Client's Address (ZIP)
    kon_ort=fields.Char("Ort")#Client's Address (city)
    kon_bundesland=fields.Selection(String="Bundesland", selection=[('bw', 'Baden-Württemberg'),#Client's Address (state)
                                            ('Bayern','Bayern'),
                                            ('Berlin','Berlin'),
                                            ('Brandenburg', 'Brandenburg'),
                                            ('Bremen', 'Bremen'),
                                            ('Hamburg', 'Hamburg'),
                                            ('Hessen', 'Hessen'),
                                            ('Mecklrnburg-Vorpommern', 'Mecklenburg-Vorpommern'),
                                            ('Niedersachsen', 'Niedersachsen'),
                                            ('Nordrhein-Westfalen', 'Nordrhein-Westfalen'),
                                            ('Rheinland-Pfalz', 'Rheinland-Pfalz'),
                                            ('Saarland', 'Saarland'),
                                            ('Sachsen', 'Sachsen'),
                                            ('Sachsen-Anhalt', 'Sachsen-Anhalt'),
                                            ('Schleswig-Holstein', 'Schleswig-Holstein'),
                                            ('Thüringen', 'Thüringen')])
    kon_land=fields.Char("Land")#Client's Address (country)
    kon_addresse=fields.Char('Adresse')#Client's Address (address)
    kon_datenok=fields.Boolean("DatenOK", default=False)#Client's data OK ? 
    partner_id=fields.Many2one('res.partner', ondelete='cascade', index=True, String="Partner")
    brach_contract=fields.Many2one('backend.kanzleien')
    
    
    @api.multi
    def _lookup_accessid(self):
        for record in self:
            record.accessid = str(record.id)
            
    @api.onchange('kon_vorname','kon_anrede','kon_titel')
    def _auto_vornamename(self):
        self.kon_vornamenachname =str (self.kon_anrede)+" "+str(self.kon_titel)+" "+ str(self.kon_vorname) + " , " + str(self.kon_nachname)
        self.kon_nachnamevorname =str(self.kon_nachname) + " , " + str(self.kon_vorname)
     