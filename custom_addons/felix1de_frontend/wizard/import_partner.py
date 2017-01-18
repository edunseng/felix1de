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
                                     ('mapping_data','Mapping Data')],'Partner Data Type')
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
        from pprint import pprint as pp
        print"==================", pp(partner_data)
        for line in partner_data:
            dic={}
            print"line=======>",line
            from pprint import pprint as pp
            print pp(line)
            if file_name.partner_type == 'mandantain' :
                dic.update({
                    'ist_mandant':True,
                    'ist_kontakt':False,
                    'street':line.get('Adresse',''),
                    'name':line.get('Mandant',''),
                    'BIC':line.get('BIC',''),
                    'email':line.get('eMailPISA','')
                    })
            if file_name.partner_type == 'kontakte' :
                dic.update({
                    'ist_kontakt':True,
                    'ist_mandant':False,
                    'street':line.get('Adresse',''),
                    'name':line.get('Nachname',''),
                    'lastname':line.get('NachnameVorname',''),
                    'phone':line.get('Telefon1',''),
                    'email':line.get('eMail1',''),
                    'company_type':'person'
                    })
            
            if file_name.partner_type in ('kontakte','mandantain'):
                partner_id = self.pool.get('res.partner').create(cr,uid,dic,context=None)
                print "partner_id===============>",partner_id
                self.pool.get('bank.detail').create(cr,uid,{
                                                    'iban':line.get('IBAN',''),
                                                    'name':line.get('Bank',''),
                                                    'bic':line.get('BIC',''),
                                                    'client_number':line.get('Mandantennummer',''),
                                                    'client_id':partner_id,
                    })
            if file_name.partner_type == 'mapping_data' :
                kontakt_id = partner_pool.search(cr,uid,[('name','=',str(line.get('Nachname','')))],limit=1)
                mandant_id = partner_pool.search(cr,uid,[('name','=',str(line.get('Vorname','')))],limit=1)
                print"kontakt_id===>",kontakt_id
                print"mandant_id======>",mandant_id
                if kontakt_id and mandant_id :
                    partner_pool.write(cr,uid,mandant_id,{
                        'child_ids':[(6,0,kontakt_id)]
                        })
            return True
    
res_partner_import()
    
    