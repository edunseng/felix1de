# -*- coding: utf-8 -*-
from openerp import models, fields,api


class TodoWorkflow(models.Model):
    _name = 'todo.workflow'
    _rec_name = 'user_id'
    _inherit = ['mail.thread']
    
    description = fields.Char('Beschreibung', required=True,help="Was soll gemacht werden?")
    is_done = fields.Boolean('Erledigt?')
    active = fields.Boolean('Aktiv?')
    user_id = fields.Many2one('res.users', 'Verantwortlich')
    date_deadline = fields.Date('Deadline')
    
    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True

 #   @api.multi
 #   def do_clear_done(self):
 #       done_recs = self.search([('is_done', '=', True)])
 #       done_recs.write({'active': False})
 #       return True

    @api.multi
    def do_clear_done(self):
        domain = [('is_done', '=', True),'|', ('user_id', '=', self.env.uid),('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True



    @api.one
    def do_toggle_done_own(self):
        if self.user_id != self.env.user:
            raise Exception ('Nur der fuer diese Aufgabe verantwortliche kann das ausfuehren!')
        else:
            self.is_done = not self.is_done
            #return super(TodoWorkflow, self).do_toggle_done()
            
            
            
            