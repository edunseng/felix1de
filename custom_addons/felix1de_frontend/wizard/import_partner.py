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

class res_partner_import(models.Model):
    _name='res.partner.import'
    partner_type = fields.Selection([('mandantain','Mandanten'),
                                     ('kontakte','Kontakte')],'Partner Data Type')
    data = fields.Binary('Data')
    
    
     
    def import_partner_data(self, cr, uid, ids, context=None):
        file_name = self.browse(cr, uid, ids)[0]
        if not file_name.data:
            raise osv.except_osv(_('File Not Chosen!'), _('Please Choose The File!'))
        str_data = base64.decodestring(file_name.data)
        if not str_data:
            raise osv.except_osv('Warning', 'No File Data')
        try:
            partner_data = csv.DictReader(cStringIO.StringIO(str_data), dialect="excel")
            # saleorder_data = list(csv.reader(cStringIO.StringIO(str_data)))
        except:
            raise osv.except_osv('Warning', 'Make sure you saved the file as .csv extension and import!')
        for line in partner_data:
            dic={}
            print"line=======>",line
            from pprint import pprint as pp
            print pp(line)
            if file_name.is_mandant :
                dic.update({
                    'ist_mandant':True,
                    'is_kontakt':False,
                    'street':line.get('Adresse',''),
                    'name':line.get('Mandant',''),
                    'BIC':line.get('BIC',''),
                    'email':line.get('eMailPISA','')
                    })
            self.pool.get('res.partner').create(cr,uid,dic
                )
            if file_name.is_kontakt :
                dic.update({
                    'is_kontakt':True,
                    'ist_mandant':False,
                    'street':line.get('Adresse',''),
                    'name':line.get('Mandant',''),
                    'BIC':line.get('BIC',''),
                    'email':line.get('eMailPISA','')
                    })
            partner_id = self.pool.get('res.partner').create(cr,uid,dic,context=None)
            self.pool.get('bank.detail').create({
                                                'iban':line.get('IBAN',''),
                                                'name':line.get('Bank',''),
                                                'bic':line.get('BIC',''),
                                                'client_number':line.get('Mandantennummer','')
                })
            
            #count += 1
            #emp_name = line.get('Name',False)
            #other = [l.replace('/t', ',') for l in line]
            #other1 = other[0].split()
            #date = line.get('Date',False)
            #status = line.get('Status',False)
            #if not emp_name or not date:
            #    raise osv.except_osv(
            #            _('-'),
            #            _('Any Column is blank in Row No %s ') % (count))

    
res_partner_import()
    
    