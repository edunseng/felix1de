from openerp import models, fields, api,_

class backend_kanzleien(models.Model):
    _inherit='backend.kanzleien'
    
    branch=fields.Many2one('backend.mandanten')
    brach_contract_rel=fields.One2many('backend.kontakte','brach_contract')
    contact_person_id=fields.One2many('backend.kontakte','brach_contract')
    branch_phone=fields.Char('branch phone')
    address=fields.Char('Address')
    branch_street=fields.Char('branch_street')
    branch_street_no=fields.Char('branch_street_no')
    branch_house_no=fields.Char('branch_house_no')
    branch_street_extra=fields.Char('branch_street_extra')
    branch_city=fields.Char('branch_city')
    branch_post_code=fields.Char('branch_post_code')
    branch_mail=fields.Char('branch_mail')
    branch_city_extra=fields.Char('branch_city_extra')
    
    
