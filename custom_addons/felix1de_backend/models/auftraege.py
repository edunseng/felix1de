# -*- coding: utf-8 -*-

from openerp import models, fields, api,_
import methods

class backend_auftraege(models.Model):
    _name='backend.auftraege'
    _rec_name = 'auf_mandant'  # the default
    _order = 'auf_mandant,id'
    _description = "Mandanten Main Model"    
    #_inherit='sale.order'
    
    
    auf_accessid=fields.Char('ID', compute='_lookup_accessid')
    
    auf_mandant=fields.Many2one("backend.mandanten", string="Mandant",index=True, ondelete='set null')
    auf_buchungsdatum=fields.Date("Buchungsdatum")
    auf_paket=fields.Many2one("backend.pakete", string="Pakete", index=True, ondelete='set null')
    auf_start=fields.Date("Start")
    auf_ende=fields.Date("Ende")
    auf_umsatz=fields.Monetary("Umsatz")
    auf_bruttoeinnahmen=fields.Monetary("Bruttoeinnahmen")
    auf_arbeitnehmer=fields.Integer("Arbeitnehmer")
    auf_gebuehrmonatsonst=fields.Monetary("GebuehrMonatSonst")
    auf_gebuehrmonatbetriebst=fields.Monetary("GebuehrMonatBetriebSt")
    auf_gebuehrmonatfibu=fields.Monetary("GebuehrMonatFiBu")
    auf_gebuehrmonatfibuueberw=fields.Monetary("GebuehrMonatFiBuUeberw")
    auf_gebuehreinmalsonst=fields.Monetary("GebuehrEinmalSonst")
    auf_gebuehreinmalbetriebst=fields.Monetary("GebuehrEinmalBetriebSt")
    auf_gebuehreinmalfibu=fields.Monetary("GebuehrEinmalFiBu")
    auf_gebuehreinmalfibuueberw=fields.Monetary("GebuehrEinmalFiBuUeberw")
    auf_gebuehrjahrsonst=fields.Monetary("GebuehrJahrSonst")
    auf_gebuehrjahrbetriebst=fields.Monetary("GebuehrJahrBetriebSt")
    auf_gebuehrjahrfibu=fields.Monetary("GebuehrJahrFiBu")
    auf_gebuehrjahrfibuueberw=fields.Monetary("GebuehrJahrFiBuUeberw")
    auf_gebuehrmonat=fields.Monetary("GebuehrMonat")
    auf_gebuehreinmal=fields.Monetary("GebuehrEinmal")
    auf_gebuehrjahr=fields.Monetary("GebuehrJahr")
    auf_bemerkung=fields.Text("Bemerkung")
    auf_start1=fields.Date("Start1")
    auf_ende1=fields.Date("Ende1")
    auf_umsatz1=fields.Monetary("Umsatz1")
    auf_bruttoeinnahmen1=fields.Monetary("Bruttoeinnahmen1")
    auf_arbeitnehmer1=fields.Integer("Arbeitnehmer1")
    auf_gebuehrmonatsonst1=fields.Monetary("GebuehrMonatSonst1")
    auf_gebuehrmonatbetriebst1=fields.Monetary("GebuehrMonatBetriebSt1")
    auf_gebuehrmonatfibu1=fields.Monetary("GebuehrMonatFiBu1")
    auf_gebuehrmonatfibuueberw1=fields.Monetary("GebuehrMonatFiBuUeberw1")
    auf_gebuehreinmalsonst1=fields.Monetary("GebuehrEinmalSonst1")
    auf_gebuehreinmalbetriebst1=fields.Monetary("GebuehrEinmalBetriebSt1")
    auf_gebuehreinmalfibu1=fields.Monetary("GebuehrEinmalFiBu1")
    auf_gebuehreinmalfibuueberw1=fields.Monetary("GebuehrEinmalFiBuUeberw1")
    auf_gebuehrjahrsonst1=fields.Monetary("GebuehrJahrSonst1")
    auf_gebuehrjahrbetriebst1=fields.Monetary("GebuehrJahrBetriebSt1")
    auf_gebuehrjahrfibu1=fields.Monetary("GebuehrJahrFiBu1")
    auf_gebuehrjahrfibuueberw1=fields.Monetary("GebuehrJahrFiBuUeberw1")
    auf_fibuaufsage=fields.Boolean("FiBuAufSage", default=False)
    auf_fibuaufsage1=fields.Boolean("FiBuAufSage1", dafault=False)
    auf_ersteller=fields.Char("Ersteller")
    auf_angelegtam=fields.Date("AngelegtAm")
    auf_angelegtvon=fields.Char("AngelegtVon")
    auf_auftragswert=fields.Monetary("Auftragswert")
    auf_datenok=fields.Boolean("DatenOK", default=False)
    auf_abgerechnet=fields.Boolean("Abgerechnet", default=False)
    currency_id=fields.Many2one('res.currency', string="Währung")
    
    
    @api.multi
    def _lookup_accessid(self):
        for record in self:
            record.accessid = str(record.id)