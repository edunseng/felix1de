from openerp import models, fields, api,_

class backend_auftraege(models.Model):
    _name='backend.auftraege' 
    _inherit=['backend.auftraege','mail.thread']
    
    product_id=fields.One2many('backend.auftraege_preise', 'auftrag_id')
   
	
   
class backend_auftraege(models.Model):
    _name='backend.auftraege_preise'
    
    auftrag_id=fields.Many2one('backend.auftraege')
    name=fields.Char('Name')
    monatsgebuhr=fields.Float('Monatsgebuhr')
    einmalgebuhr=fields.Float('Einmalgebuhr')
    jahresgebuhr=fields.Float('Jahresgebuhr')
    order_id=fields.Many2one('client.order')
    
class backend_auftraege(models.Model):
    _name='backend.line'