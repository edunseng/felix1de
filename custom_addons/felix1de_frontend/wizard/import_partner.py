# -*- coding: utf-8 -*-

import json
from lxml import etree
from datetime import datetime
from openerp import api, fields, models, _
from openerp.osv import osv
import csv
import base64
import StringIO
import cStringIO 
from xlrd import open_workbook

class res_partner_import(models.Model):
    _name='res.partner.import'
    partner_type = fields.Selection([('mandantain','Mandanten'),
                                     ('kontakte','Kontakte'),
                                     ( 'mapping_data_mandant', 'Mapping Data Mandant' ),
                                     ( 'mapping_data_kontakt', 'Mapping Data Kontakt' )], 'Partner Data Type' )
    data = fields.Binary('Data')
    
    def import_excel_sheet(self, cr, uid, ids, context=None):
        partner_pool = self.pool.get('res.partner')
        file_name = self.browse(cr, uid, ids)[0]
        if not file_name.data:
            raise osv.except_osv(_('File Not Chosen!'), _('Please Choose The File!'))
        str_data = base64.decodestring(file_name.data)
        if not str_data:
            raise osv.except_osv('Warning', 'No File Data')
        try:
            partner_data = csv.DictReader(cStringIO.StringIO(str_data), delimiter=',', quotechar='"')
        except:
            raise osv.except_osv('Warning', 'Make sure you saved the file as .csv extension and import!')
        count=0
        for line in partner_data:
            count+=1
            kontakt_id = partner_pool.search(cr,uid,[('name','=',str(line.get('Nachname',''))),('ist_kontakt','=',True)],limit=1)
            mandant_id = partner_pool.search(cr,uid,[('name','=',str(line.get('Mandant',''))),('ist_mandant','=',True)],limit=1)
            print"kontakt_id",kontakt_id
            print"mandant_id",mandant_id
            print"count",count
            if kontakt_id and mandant_id :
                partner_pool.write(cr,uid,mandant_id,{
                    'child_ids':[(6,0,kontakt_id)]
                    })
     
    def import_partner_data(self, cr, uid, ids, context=None):
        partner_pool = self.pool.get('res.partner')
        file_name = self.browse(cr, uid, ids)[0]
        partner_data=''
        if not file_name.data:
            raise osv.except_osv(_('File Not Chosen!'), _('Please Choose The File!'))
        str_data = base64.decodestring(file_name.data)
        print "str_data=========>",str_data
        if not str_data:
            raise osv.except_osv('Warning', 'No File Data')
        try:
            partner_data = csv.DictReader(cStringIO.StringIO(str_data), delimiter=',', quotechar='"')
            # saleorder_data = list(csv.reader(cStringIO.StringIO(str_data)))
        except:
            raise osv.except_osv('Warning', 'Make sure you saved the file as .csv extension and import!')
        for line in partner_data:
            dic={}
            bank_dic = {}
            from pprint import pprint as pp
            print"lines====>", pp(line)
            if file_name.partner_type == 'mandantain' :
                dic.update({
                    'ist_mandant':True,
                    'ist_kontakt':False,
                    'street':line.get('Adresse',''),
                    'name':line.get('Mandant',''),
                    'email':line.get('eMailPISA',''),
                    'name':line.get('Mandant',''),
                    'complete_name':line.get('Mandant',''),
                    'record_id':line.get('ID',''),
                    'mandantennummer':line.get('Mandantennummer',''),
                    'kanzlei':line.get('Kanzlei',''),
                    'steuerberater':line.get('Steuerberater',''),
                    'unternehmensform':line.get('Unternehmensform',''),
                    'branche':line.get('Branche'),
                    'Status':line.get('Status',''),
                     'bemerkung':line.get('Bemerkung',''),
                     'empfaenger1':line.get('Empfaenger1',''),
                     'empfaenger2':line.get('Empfaenger2',''),
                     'strasse':line.get('Strasse',''),
                     'hausnummer':line.get('Hausnummer',''),
                     'plz':line.get('PLZ'),
                     'ort':line.get('Ort'),
                     'bundesland':line.get('Bundesland'),
                     'land':line.get('Land',''),
                     'Kontoinhaber':line.get('Kontoinhaber',''),
                     'phone':line.get('Telefon1',''),
                     'telefon2':line.get('Telefon2',''),
                     'eMail1':line.get('eMail1',''),
                     'eMail2':line.get('eMail2',''),
                     'datenok':line.get('DatenOK',''),
                    })
            if file_name.partner_type == 'kontakte' :
                dic.update({
                    'ist_mandant':False,
                    'ist_kontakt':True,
                    'name':line.get('Vorname','') or line.get('Nachname','') or line.get('NachnameVorname',''),
                    'lastname':line.get('Nachname',''),
                    'complete_name':line.get('NachnameVorname',''),
                    'street':line.get('Adresse',''),
                    #'name':line.get('Mandant',''),
                    'email':line.get('eMailPISA',''),
                    'record_id':line.get('ID',''),
                    'mandantennummer':line.get('Mandantennummer',''),
                    'kanzlei':line.get('Kanzlei',''),
                    'steuerberater':line.get('Steuerberater',''),
                    'unternehmensform':line.get('Unternehmensform',''),
                    'branche':line.get('Branche'),
                    'status':line.get('Status',''),
                    'bemerkung':line.get('Bemerkung',''),
                    'empfaenger1':line.get('Empfaenger1',''),
                    'empfaenger2':line.get('Empfaenger2',''),
                    'strasse':line.get('Strasse',''),
                    'hausnummer':line.get('Hausnummer',''),
                    'plz':line.get('PLZ'),
                    'ort':line.get('Ort'),
                    'bundesland':line.get('Bundesland'),
                    'land':line.get('Land',''),
                    'Kontoinhaber':line.get('Kontoinhaber',''),
                    'phone':line.get('Telefon1',''),
                    'telefon2':line.get('Telefon2',''),
                    'eMail1':line.get('eMail1',''),
                    'eMail2':line.get('eMail2',''),
                    'datenok':line.get('DatenOK',''),
                    })
            if file_name.partner_type in ('kontakte','mandantain'):
                partner_id = self.pool.get('res.partner').create(cr,uid,dic,context=None)
                print "partner_id===============>",partner_id
                if line.get('Bank',''):
                    bank_dic.update({
                        'name':line.get('Bank',''),
                        'bic':line.get('BIC',''),
                        'iban':line.get('IBAN',''),
                        'client_number':line.get('Mandantennummer',''),
                        'client_id':partner_id,
                        'parent_id':partner_id,
                        'account_number':line.get('Kontoinhaber','')
                    })
                    self.pool.get('bank.detail').create(cr,uid,bank_dic)
            if file_name.partner_type == 'mapping_data_mandant' :
                cr.execute( "select id from res_partner where record_id = '%s'" % ( str( line.get( 'Kontakt', '' ) ) ) )
                kontakt_id = cr.fetchone()
                cr.execute( "select id from res_partner where record_id = '%s'" % ( str( line.get( 'Mandant', '' ) ) ) )
                mandant_id = cr.fetchone()
                # mandant_id = partner_pool.search(cr,uid,[('record_id','=',str(line.get('Mandant','')))],limit=1)
                print"kontakt_id===>", kontakt_id
                print"mandant_id======>", mandant_id
                if kontakt_id and mandant_id :
                    print"inside the mandant and kontakt"
                    partner_pool.write( cr, uid, mandant_id[0], {
                        'mandant_child_ids':[( 6, 0, [kontakt_id[0]] )]
                        })
            if file_name.partner_type == 'mapping_data_kontakt' :
                cr.execute( "select id from res_partner where record_id = '%s'" % ( str( line.get( 'Kontakt', '' ) ) ) )
                kontakt_id = cr.fetchone()
                cr.execute( "select id from res_partner where record_id = '%s'" % ( str( line.get( 'Mandant', '' ) ) ) )
                mandant_id = cr.fetchone()
                print"mandant_id======>", mandant_id
                if kontakt_id and mandant_id :
                    print"inside the mandant and kontakt"
                    partner_pool.write( cr, uid, kontakt_id[0], {
                        'kontact_child_ids':[( 6, 0, [mandant_id[0]] )]
                        } )
        return True
    
res_partner_import()
    
    
