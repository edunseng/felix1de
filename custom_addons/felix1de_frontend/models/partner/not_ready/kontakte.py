from openerp import models, fields, api,_

class PartnerKontakte(models.Model):
   # _name='backend.kontakte'
    
    _inherits={'backend.kontakte':'kontakte_id'}
    _inherit='res.partner'
    
    kontakte_id=fields.Many2one('backend.kontakte',ondelete='cascade', String="Kontakt", index=True)
    ist_kontakt=fields.Boolean('Ist Kontakt')
    #client_id=fields.One2many('backend.mandanten', 'contact_id')
    #ticket_id=fields.One2many('felix1.ticket', 'contact_id')
   # brach_contract=fields.Many2one('backend.kanzleien')
    image=fields.Binary(String="image")
    contact_id=fields.Char(string="Contact Id")
    remark=fields.Text('Remark')
   # category_id=fields.Many2one('res.partner.category',string='Tags')
    con_acquired_by=fields.Char('Acquired By')
    contact_since=fields.Char('Kontakt seit')
    
    

