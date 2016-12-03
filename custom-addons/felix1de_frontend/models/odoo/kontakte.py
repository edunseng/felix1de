from openerp import models, fields, api,_

class backend_kontakte(models.Model):
    _name='backend.kontakte' 
    _inherit=['backend.kontakte','mail.thread'] 
    
    client_id=fields.One2many('backend.mandanten', 'contact_id')
    ticket_id=fields.One2many('felix1.ticket', 'contact_id')
    brach_contract=fields.Many2one('backend.kanzleien')
    image=fields.Binary(String="image")
    contact_id=fields.Char(string="Kontakt")
    #remark=fields.Text('Remark')
    category_id=fields.Many2one('res.partner.category',string='Tags')
    con_acquired_by=fields.Char('Gewonnen Durch')
    contact_since=fields.Char('Kontakt seit')


   # name=fields.Char('name')
   # last_name=fields.Char('last name') 

   