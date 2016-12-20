# -*- coding: utf-8 -*-
from openerp import fields, models, api


_EKS_LIST = [
    ('1', 'Prüfung: Eingang Einkommensteuer-FB'),
    ('2', 'Anruf beim Mandanten'),
    ('3', 'Eingang Einkommensteuer-FB'),
    ('4', ' Anruf beim Mandanten'),
    ('5', 'Prüfung: Eingang Einkommensteuer-Fragebogen'),
    ('6', 'Erinnerung Mandant per Mail'),
    ('7', 'Eingang des Fragebogens'),
    ('8', 'Weiterleitung des Fragebogens')]


_GRUENDUNG_LIST = [
    ('1', 'Willkommens-Mail senden'),
    ('2', 'Mandant anrufen'),
    ('3', 'Online-Fragebogen an den Mandantensenden'),
    ('4', 'Prüfung Erhalt Online-Fragebogen'),
    ('5', 'Dokumente erstellen'),
    ('6', 'IHK-Dokumente'),
    ('7', 'Mail an RA Hahn'),
    ('8', 'Notartermin'),
    ('9', 'Mandanten informieren'),
    ('10', 'Unterlagen an Notar senden'),
    ('11', 'Weiterleitung Unterlagen an StB'),
    ('12', 'Nach Notartermin Urkunden vom Notar anfordern'),
    ('13', 'Rückmeldung vom StB')]


_ONBOARDING_LIST = [
    ('1', 'Willkommens-Mail senden'),
    ('2', 'Mandant anrufen'),
    ('3', 'Online-Fragebogen an den Mandantensenden'),
    ('4', 'Prüfung Erhalt Online-Fragebogen'),
    ('5', 'Dokumente erstellen'),
    ('6', 'IHK-Dokumente'),
    ('7', 'Mail an RA Hahn'),
    ('8', 'Notartermin'),
    ('9', 'Mandanten informieren'),
    ('10', 'Unterlagen an Notar senden'),
    ('11', 'Weiterleitung Unterlagen an StB'),
    ('12', 'Nach Notartermin Urkunden vom Notar anfordern'),
    ('13', 'Rückmeldung vom StB')]

_ORDENTLICHE_KUENDIGUNG_LIST = [
    ('1', 'Willkommens-Mail senden'),
    ('2', 'Mandant anrufen'),
    ('3', 'Online-Fragebogen an den Mandantensenden'),
    ('4', 'Prüfung Erhalt Online-Fragebogen'),
    ('5', 'Dokumente erstellen'),
    ('6', 'IHK-Dokumente'),
    ('7', 'Mail an RA Hahn'),
    ('8', 'Notartermin'),
    ('9', 'Mandanten informieren'),
    ('10', 'Unterlagen an Notar senden'),
    ('11', 'Weiterleitung Unterlagen an StB'),
    ('12', 'Nach Notartermin Urkunden vom Notar anfordern'),
    ('13', 'Rückmeldung vom StB')]

_UMZUG_LIST = [
    ('1', 'Willkommens-Mail senden'),
    ('2', 'Mandant anrufen'),
    ('3', 'Online-Fragebogen an den Mandantensenden'),
    ('4', 'Prüfung Erhalt Online-Fragebogen'),
    ('5', 'Dokumente erstellen'),
    ('6', 'IHK-Dokumente'),
    ('7', 'Mail an RA Hahn'),
    ('8', 'Notartermin'),
    ('9', 'Mandanten informieren'),
    ('10', 'Unterlagen an Notar senden'),
    ('11', 'Weiterleitung Unterlagen an StB'),
    ('12', 'Nach Notartermin Urkunden vom Notar anfordern'),
    ('13', 'Rückmeldung vom StB')]

_UMSATZANPASSUNG_LIST = [
    ('1', 'Willkommens-Mail senden'),
    ('2', 'Mandant anrufen'),
    ('3', 'Online-Fragebogen an den Mandantensenden'),
    ('4', 'Prüfung Erhalt Online-Fragebogen'),
    ('5', 'Dokumente erstellen'),
    ('6', 'IHK-Dokumente'),
    ('7', 'Mail an RA Hahn'),
    ('8', 'Notartermin'),
    ('9', 'Mandanten informieren'),
    ('10', 'Unterlagen an Notar senden'),
    ('11', 'Weiterleitung Unterlagen an StB'),
    ('12', 'Nach Notartermin Urkunden vom Notar anfordern'),
    ('13', 'Rückmeldung vom StB')]

class StatusChange(models.Model):
    _name='project.states'

    _KATEGORY_LIST = [
        ('einkommensteuer', 'Einkommensteuer-FB'),
        ('gruendung', 'Gruendung'),
        ('onoarding', 'Onoarding'),
        ('ordentliche_kuendigung', 'ordentliche Kuendigung'),
        ('umsatzanpassung', 'Umsatzanpassung'),
        ('umzug', 'Umzug')]

    category=fields.Selection(selection=_KATEGORY_LIST,string='Kateghorie', default=_KATEGORY_LIST[0][0], store=True)
    descriotion=fields.Html('Beschreibung')
    
#    @api.depends(category)

 #   def on_category_change(category):
 #       if self.category in 
 #           self.categoryrint 'Hello'
#           status=fields.Selection([_GRUENDUNG_LIST[0],_GRUENDUNG_LIST[1],_GRUENDUNG_LIST[2],
 #                            _GRUENDUNG_LIST[3],_GRUENDUNG_LIST[4]], string='Status2',  
 #                            default=_GRUENDUNG_LIST[0][0],track_visibility = 'onchange')#allways
 
class ProjectIssue(models.Model):
    _name='project.issue'
    _inherit=['project.task','project.issue','project.states']
    prm_ticket_id=fields.Char('Ticket-ID')
    mitarbeiter_id=fields.Many2one('felix1.employees',"Zugewiesener Mitarbeiter")
    backend_kontakte_id=fields.Many2one('backend.kontakte', string="kontakte")
    ChamBranch_rel=fields.Many2one('branch.branch', string="Kanzlei-Niederlassung")
    ToDoPhone=fields.Char( string="Telefon" , related="partner_id.phone")
    rem_Content=fields.Text('Problemloesung')
    frkKathegory_id=fields.Many2one('felix1.ticket.kathegoriess', string='Kathegorie')
    tikDueDate=fields.Date('Faellig Am')
    mandanten_id=fields.Many2one('backend.mandanten', string="Mandanten")
    frkRemark=fields.Text('Bemerkung')
    tikStartDate=fields.Date('Erstellt Am')
    tikCloseDate=fields.Date('Geschlossen Am')
    ticket_id=fields.Many2one('felix1.ticket', string="Ticket")
    priority = fields.Selection([('0','Low'), ('1','Normal'),('2','Intermediate'),('3','High')], 'Priority', select=True) 
    tikmarkopen=fields.Boolean('Vormerken')
    statusbar_einkommensteuer=fields.Selection([_EKS_LIST[0],_EKS_LIST[1],_EKS_LIST[2],_EKS_LIST[3],_EKS_LIST[4]], string='Status', default=_EKS_LIST[0][0],track_visibility = 'onchange')#allways
    statusbar_gruendung=fields.Selection([_GRUENDUNG_LIST[0],_GRUENDUNG_LIST[1],_GRUENDUNG_LIST[2], _GRUENDUNG_LIST[3],_GRUENDUNG_LIST[4]], string='Status', default=_GRUENDUNG_LIST[0][0],track_visibility = 'onchange')#allways
    statusbar_onoarding=fields.Char()
    statusbar_ordentliche_kuendigung=fields.Char()
    statusbar_umsatzanpassung=fields.Char()
    statusbar_umzug=fields.Char()
    hidestage=fields.Boolean(default=True)
    
    #relinputfeld=fields.Many2one('project.task.type')
    #state=fields.Selection(
    #    related='relinputfeld.inputfeld', store=True, readonly=True)
    

    @api.one
    def do_toggle_mode(self):
        self.tikmarkopen = not self.tikmarkopen
        return True
    
    # progress to first state
    @api.multi
    def EKS_progress_value(self):
        self.write({'statusbar_einkommensteuer':'2'})
    def GRUENDUNG_progress_value(self):
        self.write({'statusbar_gruendung':'2'})    
    def ONBOARDING_progress_value(self):
        self.write({'statusbar_onoarding':'2'})
    def ORDENTLICHE_KUENDIGUNG_progress_value(self):
        self.write({'statusbar_ordentliche_kuendigung':'2'})
    def UMZUG_progress_value(self):
        self.write({'statusbar_umzug':'2'})
    def UMSATZANPASSUNG_progress_value(self):
        self.write({'statusbar_umsatzanpassung':'2'})

        
        
    @api.multi
    def cancel_value(self):
        self.write({'status':'cancelled'})
    @api.multi
    def done_value(self):
        self.write({'status':'done'})
        
class BackendLine(models.Model):
    _name='prject.task.line'

    line=fields.Many2one('project.task')
    name=fields.Char('Name')
    monatsgebuhr=fields.Float('Monatsgebuhr')
    einmalgebuhr=fields.Float('Einmalgebuhr')
    jahresgebuhr=fields.Float('Jahresgebuhr')
    #order_id=fields.Many2one('client.order')
    
class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'
#    state = fields.Selection(_EKS_LIST, 'State')
#    status2 = fields.Selection(_GRUENDUNG_LIST, 'State')


class ProjectTask(models.Model):
    _inherit='project.task'

    # Fields were not in the model so copied from project.task.line to get them in the view
    monatsgebuhr=fields.Float('Monatsgebuhr')
    einmalgebuhr=fields.Float('Einmalgebuhr')
    jahresgebuhr=fields.Float('Jahresgebuhr')
    product_id=fields.One2many('prject.task.line', 'line')
    
 #   state = fields.Selection(
 #       related='stage_id.state', store=True, readonly=True)
 #   mask = fields.Selection(
 #       related='stage_id.mask', store=True, readonly=True)


#    @api.model
#    def _init_fold_statusbar(self):
#        """ On module install initialize fold_statusbar values """
#        for rec in self.search([]):
#            rec.fold_statusbar = rec.fold

