from openerp import models, fields, api,_

class backend_mandanten(models.Model):
    _name='backend.mandanten' 
    _inherit=['backend.mandanten','mail.thread'] 
    
    contact_id=fields.Many2one('backend.kontakte', string='Contact ID')
    bank_rel=fields.One2many('bank.detail', 'mandant_id')
    order_id=fields.One2many('client.order', 'client_order_id')
    number_id=fields.One2many('client.number', 'name')
    ticketing_rel=fields.One2many('felix1.ticket','priPriority')
    branch_id=fields.One2many('backend.kanzleien','branch')
    image=fields.Binary(String="image")
    
