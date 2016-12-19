# -*- coding: utf-8 -*-


from openerp import models, fields, api


_TASK_STATE = [
    ('draft', 'New'),
    ('open', 'In Progress'),
    ('pending', 'Pending'),
    ('done', 'Done'),
    ('cancelled', 'Cancelled')]


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'
    state = fields.Selection(_TASK_STATE, 'State',default=_TASK_STATE[0])
    fold_statusbar = fields.Boolean('Folded in Statusbar')

    @api.model
    def _init_fold_statusbar(self):
        """ On module install initialize fold_statusbar values """
        for rec in self.search([]):
            rec.fold_statusbar = rec.fold
            



class ProjectTask(models.Model):
    _inherit = 'project.task'
    state = fields.Selection(
        related='stage_id.state', store=True, readonly=True)
