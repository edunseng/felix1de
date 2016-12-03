# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
from datetime import time, datetime
import apiais

class backend_kanzleien(models.Model):
    _name='backend.kanzleien'
    _inherit='backend.apiais.accessid'
    
    accessid=fields.Char('ID', compute='_lookup_accessid')
    
    name=fields.Char(String="Niederlassung", help="Name des Niederlassung")
    bemerkung=fields.Text('Bemerkung')
    f1kanzleinummer=fields.Char('f1KanzleiNummer')
    hausnr=fields.Char('Hausnummer')
    Strasse=fields.Char('Straße')
    strassezusatz=fields.Char('Straße(Zusatz)')
    plz=fields.Char('PLZ')
    ort=fields.Char('Ort')
    ortzusatz=fields.Char('Ort(Zusatz)')
    email=fields.Char('Email')
    vertragsart=fields.Char('Vertragsart')
    etaxberaternummer=fields.Char('ETAXBeraternummer')
    Lohnberaternummer=fields.Char('Lohnberaternummer')
    reweTestkanzlei=fields.Boolean('reweTestkanzlei')
    sageaccedition=fields.Boolean('Sage Acc Edition')
    virtuellesetax=fields.Char('virtuelles ETAX')
    etlnummerstammkanzlei=fields.Char('ETL Nummer Stammkanzlei')
    namestammkanzlei=fields.Char('Stammkanzlei (Name)')
    ortstammkanzlei=fields.Char('Stammkanzlei (Ort)')
    datenok=fields.Boolean('Daten OK')
    beitragmonatlich=fields.Monetary("Beitrag (monatlich)")
    beitragberechnetjahr=fields.Monetary("Beitrag (jährlich)")
    beitragmonatlichreduziert=fields.Monetary("Beitrag (monatlich reduziert)")
    beitragberechnetjahrreduziert=fields.Monetary("Beitrag (jährlich reduziert)")
    startdatum=fields.Date('Datum (start)')
    kuendigungdatum=fields.Date('Datum (Kündigung)')
    ausgesetztbis=fields.Date('Ausgesetzt Bis')
    scsbereich=fields.Char('SCSBereich')
    currency_id=fields.Many2one('res.currency', string='Währung')

   
        