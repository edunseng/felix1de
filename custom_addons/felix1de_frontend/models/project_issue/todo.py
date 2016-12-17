# -*- coding: utf-8 -*-
from openerp import models, fields
class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char('Beschreibung', required=True)
    is_done = fields.Boolean('Erledigt?')
    active = fields.Boolean('Aktiv?', default=True)