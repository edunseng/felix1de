# -*- coding: utf-8 -*-
from openerp import fields, models, api


_KATEGORY_LIST = [
    ('einkommensteuer', 'Einkommensteuer-FB'),
    ('gruendung', 'Gruendung'),
    ('onoarding', 'Onoarding'),
    ('ordentliche_kuendigung', 'ordentliche Kuendigung'),
    ('umsatzanpassung', 'Umsatzanpassung'),
    ('umzug', 'Umzug')]

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
    ('1', 'Anlage in der Datenbank (Status "neu")'),
    ('2', 'Identifizierung anstoßen bei natürlichen Personen'),
    ('3', 'Identifizierung von Gesellschaften'),
    ('4', 'Identifizierung erfolgt? JA/NEIN'),
    ('5', 'Klärung Unstimmigkeiten in der Buchung'),
    ('6', 'Verteilung des Mandats'),
    ('7', 'Anruf in der Kanzlei zu neuem Mandat'),
    ('8', 'Anlage ETAX + Vergabe Mdt.-Nummer (Status "im Onboarding")'),
    ('9', 'Willkommens-Mail an Mandant'),
    ('10', 'bei Lohn: gesonderte Lohn-Mail an Mandant'),
    ('11', 'Steuerberater-Wechsel-Service anstoßen!'),
    ('12', 'Info an felix1.de-NL über neues Mandat'),
    ('13', 'bei Lohn: Info an PKC'),
    ('14', 'bei Fibu über FKC: Info an FKC'),
    ('15', 'PISA Anlage'),
    ('16', 'Status setzen auf laufendes Mandat'),
    ('17', 'Bestätigung der Vertragschließung versenden'),
    ('18', 'Kontaktaufnahme beim Mandanten durch NL erfolgt?')]

_ORDENTLICHE_KUENDIGUNG_LIST = [
    ('1', 'Kündigung erhalten am:'),
    ('2', 'Pauschalen auf "beendet" setzen.'),
    ('3', 'Anruf des Mandanten zur Rückgewinnung'),
    ('4', 'Starten Prozess Kanzleiwechsel/Paketwechsel'),
    ('5', 'Bestätigung der Kündigung'),
    ('6', 'Information an die Kanzlei, PKC und FKC'),
    ('7', 'ETAX - Aufträge/Pauschalen löschen'),
    ('8', 'Prüfung Informationen aus der Kanzlei'),
    ('9', 'Rechnungslegung'),
    ('10', 'ETAX - Zuodnung löschen'),
    ('11', 'Ablage')]

_UMSATZANPASSUNG_LIST = [
    ('1', 'Jahresendabrechnung'),
    ('2', 'Liste Umsatzanpassung'),
    ('3', 'Anpassung ETAX'),
    ('4', 'Anpassung Backend'),
    ('5', 'Anpassung Datenbank')]

_UMZUG_LIST = [
    ('1', 'Info einholen von Kanzlei (FKC)'),
    ('2', 'sind Rechnungen offen?'),
    ('3', 'Anruf beim Mandanten'),
    ('4', 'Zusammenfassung an Mandant'),
    ('5', 'Endabrechnung'),
    ('6', 'Umzug in ETAXorga'),
    ('7', 'Umzug im felix1.de-Backend und PISA'),
    ('8', 'Umzug in ETAXrewe und ETAXlohn'),
    ('9', 'Umzugsliste'),
    ('10', 'Info an alle Beteiligten')]

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
    
 
class ProjectIssue(models.Model):
    _name='project.issue'
    _inherit=['project.task','project.states','project.issue']
    
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
    #status=fields.Char('Status',compute='_show_status',store=True)  #SHIVAM
    
    #status bar state fields
    statusbar_einkommensteuer=fields.Selection(_EKS_LIST,
        string='Status',
        default='1',
        track_visibility = 'onchange')#allways
    
    statusbar_gruendung=fields.Selection(_GRUENDUNG_LIST,                                         
                                          string='Status', 
                                          default='1',
                                          track_visibility = 'onchange')#allways
    statusbar_onoarding=fields.Selection(_ONBOARDING_LIST, 
                                         string='Status', 
                                         default='1',
                                         track_visibility = 'onchange')#allways
    statusbar_ordentliche_kuendigung=fields.Selection(_ORDENTLICHE_KUENDIGUNG_LIST,
                                                       string='Status',
                                                        default='1',
                                                        track_visibility = 'onchange')#allways
    statusbar_umsatzanpassung=fields.Selection(_UMSATZANPASSUNG_LIST,
                                                       string='Status', 
                                                       default='1',
                                                       track_visibility = 'onchange')#allways
    statusbar_umzug=fields.Selection(_UMZUG_LIST,                                         
                                          string='Status', default='1',track_visibility = 'onchange')#allways
    hidestage=fields.Boolean(default=True)
    #category_id  = fields.many2one('project.states','Kateghorie')
        
    
    

    
    

#    @api.one                        #SHIVAM
#    @api.depends(category)
#    def _show_status(self,category):
#   if category == "einkommensteuer":
#        self.status = "statusbar_einkommensteuer"
#    if category == "gruendung":
#        self.status = "statusbar_gruendung"
        

    

    @api.one
    def do_toggle_mode(self):
        self.tikmarkopen = not self.tikmarkopen
        return True
    
 # progress to FIRST STATE
    @api.multi
    def EKS_progress_value(self):
        status = str(self.statusbar_einkommensteuer)
        if status == '1':
            self.write({'statusbar_einkommensteuer':'2'})
        if status == '2':
            self.write({'statusbar_einkommensteuer':'3'})
        if status == '3':
            self.write({'statusbar_einkommensteuer':'4'})
        if status == '4':
            self.write({'statusbar_einkommensteuer':'5'})
        if status == '5':
            self.write({'statusbar_einkommensteuer':'6'})
        if status == '6':
            self.write({'statusbar_einkommensteuer':'7'})
        if status == '7':
            self.write({'statusbar_einkommensteuer':'8'})
        return True
        
        
    @api.multi
    def GRUENDUNG_progress_value(self):
        status = str(self.statusbar_gruendung)
        if status == '1':
            self.write({'statusbar_gruendung':'2'})
        if status == '2':
            self.write({'statusbar_gruendung':'3'})
        if status == '3':
            self.write({'statusbar_gruendung':'4'})
        if status == '4':
            self.write({'statusbar_gruendung':'5'})
        if status == '5':
            self.write({'statusbar_gruendung':'6'})
        if status == '6':
            self.write({'statusbar_gruendung':'7'})
        if status == '7':
            self.write({'statusbar_gruendung':'8'})
        if status == '8':
            self.write({'statusbar_gruendung':'9'})
        if status == '9':
            self.write({'statusbar_gruendung':'10'})
        if status == '10':
            self.write({'statusbar_gruendung':'11'})
        if status == '11':
            self.write({'statusbar_gruendung':'12'})
        if status == '12':
            self.write({'statusbar_gruendung':'13'})
        return True

    @api.multi
    def ONBOARDING_progress_value(self):
        status = str(self.statusbar_onoarding)
        if status == '1':
            self.write({'statusbar_onoarding':'2'})
        if status == '2':
            self.write({'statusbar_onoarding':'3'})
        if status == '3':
            self.write({'statusbar_onoarding':'4'})
        if status == '4':
            self.write({'statusbar_onoarding':'5'})
        if status == '5':
            self.write({'statusbar_onoarding':'6'})
        if status == '6':
            self.write({'statusbar_onoarding':'7'})
        if status == '7':
            self.write({'statusbar_onoarding':'8'})
        if status == '8':
            self.write({'statusbar_onoarding':'9'})
        if status == '9':
            self.write({'statusbar_onoarding':'10'})
        if status == '10':
            self.write({'statusbar_onoarding':'11'})
        if status == '11':
            self.write({'statusbar_onoarding':'12'})
        if status == '12':
            self.write({'statusbar_onoarding':'13'})
        if status == '13':
            self.write({'statusbar_onoarding':'14'})
        if status == '14':
            self.write({'statusbar_onoarding':'15'})
        if status == '15':
            self.write({'statusbar_onoarding':'16'})
        if status == '16':
            self.write({'statusbar_onoarding':'17'})
        return True
        
    @api.multi
    def ORDENTLICHE_KUENDIGUNG_progress_value(self):
        status = str(self.statusbar_ordentliche_kuendigung)
        if status == '1':
            self.write({'statusbar_ordentliche_kuendigung':'2'})
        if status == '2':
            self.write({'statusbar_ordentliche_kuendigung':'3'})
        if status == '3':
            self.write({'statusbar_ordentliche_kuendigung':'4'})
        if status == '4':
            self.write({'statusbar_ordentliche_kuendigung':'5'})
        if status == '5':
            self.write({'statusbar_ordentliche_kuendigung':'6'})
        if status == '6':
            self.write({'statusbar_ordentliche_kuendigung':'7'})
        if status == '7':
            self.write({'statusbar_ordentliche_kuendigung':'8'})
        if status == '8':
            self.write({'statusbar_ordentliche_kuendigung':'9'})
        if status == '9':
            self.write({'statusbar_ordentliche_kuendigung':'10'})
        if status == '10':
            self.write({'statusbar_ordentliche_kuendigung':'11'})
        
        return True
    
    
    @api.multi
    def UMZUG_progress_value(self):
        status = str(self.statusbar_umzug)
        if status == '1':
            self.write({'statusbar_umzug':'2'})
        if status == '2':
            self.write({'statusbar_umzug':'3'})
        if status == '3':
            self.write({'statusbar_umzug':'4'})
        if status == '4':
            self.write({'statusbar_umzug':'5'})
        if status == '5':
            self.write({'statusbar_umzug':'6'})
        if status == '6':
            self.write({'statusbar_umzug':'7'})
        if status == '7':
            self.write({'statusbar_umzug':'8'})
        if status == '8':
            self.write({'statusbar_umzug':'9'})
        if status == '9':
            self.write({'statusbar_umzug':'10'})
        if status == '10':
            self.write({'statusbar_umzug':'11'})
        return True
        
    @api.multi
    def UMSATZANPASSUNG_progress_value(self):
        status = str(self.statusbar_umsatzanpassung)
        if status == '1':
            self.write({'statusbar_umsatzanpassung':'2'})
        if status == '2':
            self.write({'statusbar_umsatzanpassung':'3'})
        if status == '3':
            self.write({'statusbar_umsatzanpassung':'4'})
        if status == '4':
            self.write({'statusbar_umsatzanpassung':'5'})
        return True
        
        
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

