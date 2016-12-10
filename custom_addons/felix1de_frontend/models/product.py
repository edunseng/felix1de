# -*- coding: utf-8 -*-
from openerp import models, fields, api,_

class BackendAuftraege(models.Model):
    _name='backend.auftraege'
    _inherit=['backend.auftraege','mail.thread']
    
    product_id=fields.One2many('backend.line', 'line')
   # project_task_id=fields.Many2one('project.task')
    @api.model
    def _create_project_task(self, vals):
	""" Create new project task"""
	seq = {
              'name': vals['name'],
              'product_id':vals['product_id']
                
		}
        
        return self.env['project.task'].create(seq)    

    @api.model
    def create(self, vals):
	# We just need to create the relevant id 
        projct_lst=[]
	if not vals.get('project_task_id'):
	   vals.update({'project_task_id': self.sudo()._create_project_task(vals).id}) 
         
	return super(BackendAuftraege, self).create(vals)
	
   
class backend_auftraege(models.Model):
    _name='backend.line'
    line=fields.Many2one('backend.auftraege')
    name=fields.Char('Name')
    monatsgebuhr=fields.Float('Monatsgebuhr')
    einmalgebuhr=fields.Float('Einmalgebuhr')
    jahresgebuhr=fields.Float('Jahresgebuhr')
    #order_id=fields.Many2one('client.order')
    
