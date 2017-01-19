# -*- coding: utf-8 -*-
from openerp import models, fields, api,_
import methods


class backend_berater(models.Model):
    _name='backend.berater'
    _rec_name = 'ber_nachname'  # the default
    _order = 'ber_nachname,id'
    _description = "Berater Main Model"     
    #_inherit='res.partner'
    
    ber_accessid=fields.Char('ID', compute='_lookup_accessid')
    
    ber_beraterid=fields.Char('Berater ID')
    ber_etlbenutzername=fields.Char('ETL Benutzername')
    ber_vorname=fields.Char('Vorname', help="Vorname des Steuerberaters", required=False)
    ber_nachname=fields.Char('Nachname', help="Name des Steuerberaters", required=True)
    ber_anrede=fields.Selection([(u"\u0020", 'kein'),('Herr', 'Herr'),('Frau', 'Frau')],default=u"\u0020",string="Anrede")
    ber_titel=fields.Selection(String="Titel", selection=[(u"\u0020", 'kein'),('Dr.', 'Dr.'),('Prof.','Prof.'),('Prof. Dr.','Prof. Dr.')],default= u"\u0020", string="Titel")
    ber_kanzleileiter=fields.Boolean('Kanzleileiter', dafault=False)
    ber_ansprechpartner=fields.Boolean('Ansprechpartner',default=False)
    ber_stb=fields.Boolean('StB', help="Steuerberater",default=False)
    ber_stbIn=fields.Boolean('StBIn', help="SteuerberaterIn", default=False)
    ber_ra=fields.Boolean('RA',help="Rechtsanwalt", default=False)
    ber_wp=fields.Boolean('WP', help="??", default=False)
    ber_weiteretitel=fields.Char('Weitere Titel')
    ber_hochschulabschluss=fields.Char('Hochschulabschluss')
    ber_foto=fields.Binary('Foto')
    ber_vornamenachname=fields.Char('Vorname, Nachname')
    ber_nachnamevorname=fields.Char('Nachname, Vorname')
    ber_telefon1=fields.Char('Telefon1')
    ber_telefon2=fields.Char('Telefon2')
    ber_telefon3=fields.Char('Telefon3')
    ber_email1=fields.Char('Email1')
    ber_email2=fields.Char('Email2')
    ber_email3=fields.Char('Email3')
    ber_fax=fields.Char('Fax')
    ber_bemerkung=fields.Text('Bemerkung')    
    ber_datenok=fields.Boolean('Daten OK',default=False)
    
    @api.multi
    def _lookup_accessid(self):
        for record in self:
            record.accessid = str(record.id)
            
    @api.onchange('ber_vorname','ber_anrede')
    def _auto_vornamename(self):
        self.ber_vornamenachname =str (self.ber_anrede)+" "+str(self.ber_titel)+" "+ str(self.ber_vorname) + " , " + str(self.ber_nachname)
        self.ber_nachnamevorname =str(self.ber_nachname) + " , " + str(self.ber_vorname)
    
    

    

    