from openerp import fields, models, api
class mail_followers(models.Model):
	_inherit='mail.followers'
	ticket_id=fields.Many2one('felix1.ticket')
	
class Felix1Ticket(models.Model):
	_name='felix1.ticket'
	_inherit = ['mail.thread']
	
	prm_ticket_id=fields.Char('Ticket-ID',compute='creat_ticket_id')
	name=fields.Char('Ticket')
	claticketname=fields.Char('claTicketName')
	state=fields.Selection([('new', 'Neu'),('progress','In Bearbeitung..'),('done', 'Bearbeitet'),('cancel', 'Abgebrochen')], string='Status',  default='new')
	company_id = fields.Many2one('res.company', 'Niederlassung', default=lambda self: self.env['res.company']._company_default_get('felix1.ticket'))
	mitarbeiter_id=fields.Many2one('felix1.employees',"Zugewiesener Mitarbeiter")
	priPriority=fields.Many2one('res.partner', "Ticket-Ersteller")
	#calFirstnameLastname=fields.Char(string="Zugewiesener Mitarbeiter", related="priPriority.name")
	#cal_last_name=fields.Char(string='Last Name', related='priPriority.lastname')
	conMail=fields.Char( string="Email", related="priPriority.email")
	ToDoPhone=fields.Char( string="Telefon" , related="priPriority.phone")
	tikSenderDirectDial=fields.Char('Absender Durchwahl')
	tikSenderEmail=fields.Char('Absender Email')
	tikStartDate=fields.Date('Erstellt Am')
	tikDueDate=fields.Date('Faellig Am')
	tikCloseDate=fields.Date('Geschlossen Am')
	frkKathegory_id=fields.Many2one('felix1.ticket.kathegoriess', string='Kathegorie')
	frkRemark=fields.Text('Bemerkung')
	frkChamber=fields.Char('Niederlassung')
	frmSenderChamber=fields.Char('Absender-Kanzlei')
	frmContact=fields.Many2one('felix1.contacts', 'Kontakte')
	ChamBranch_rel=fields.Many2one('branch.branch', string="Kanzlei-Niederlassung")
	ChamMail=fields.Char('Email-Kanzlei', related='ChamBranch_rel.branch_mail')
	ticketcalk=fields.Char(string="ticketingID",store=True, compute="ticketname")

		
			
	rem_Content=fields.Text('Problemloesung')
	ToDoDone=fields.Boolean('Erledigt')
	responsible=fields.Char('Verantwortlich')
	partner_id=fields.Many2one('res.partner')
	#getodoo -------
	mandanten_id=fields.Many2one('backend.mandanten', string="Mandanten")
	backend_kontakte_id=fields.Many2one('backend.kontakte', string="kontakte")
	## -------------
	ticket_id_date=fields.Date('Ticket Erstellt Am') 
	ticket_id=fields.Char('Ticket_ID')
	contact_id=fields.Many2one('contact.contacts')
	## getodoo ------------- 
	project_issue_id=fields.Many2one('project.issue') 
        @api.model 
        def _create_sequence(self, vals): 
        	""" Create new project issue""" 
        	seq = {
				'name': vals['name'], 
                'partner_id':vals['priPriority'], 
                'email_from':vals['conMail'], 
    #'prm_ticket_id':vals['prm_ticket_id'], 
                'mitarbeiter_id':vals['mitarbeiter_id'], 
                'backend_kontakte_id':vals['backend_kontakte_id'] or False, 
                'ChamBranch_rel':vals['ChamBranch_rel'], 
                'ToDoPhone':vals['ToDoPhone'], 
                'rem_Content':vals['rem_Content'], 
                'frkKathegory_id':vals['frkKathegory_id'], 
                'tikDueDate':vals['tikDueDate'], 
                'mandanten_id':vals['mandanten_id'], 
                'frkRemark':vals['frkRemark'], 
                'tikStartDate':vals['tikStartDate'], 
                'tikCloseDate':vals['tikCloseDate'], 
                'ticket_id':vals['ticket_id'], 
                 
    }
        	return self.env['project.issue'].create(seq)
        
        @api.model 
        def create(self, vals): 
        	# We just need to create the relevant id
        	if not vals.get('project_issue_id'): 
        		vals.update({'project_issue_id': self.sudo()._create_sequence(vals).id}) 
        		return super(Felix1Ticket, self).create(vals) 
 #- ----------------------------------------------------------
	#### create ticket id 
        @api.multi
	def creat_ticket_id(self):
		for record in self:
			record.prm_ticket_id= str("REFID") + str("00") + str(record.id)
	@api.multi
	def progress_value(self):
		self.write({'state':'progress'})
	@api.multi
	def cancel_value(self):
		self.write({'state':'cancel'})
	@api.multi
	def done_value(self):
		self.write({'state':'done'})
		
    
    
	
class Felix1Employees(models.Model):
	_name='felix1.employees'
	_inherit = 'hr.employee'
	name=fields.Char("Name")
class Felix1Contacts(models.Model):
	_name='felix1.contacts'
	name=fields.Char("Name")
class Felix1Chambers(models.Model):
	_name='felix1.chambers'
	name=fields.Char("Name")
	ID=fields.Integer("ID")
	chamf1ChamberNumber=fields.Char('F1-Kanzleiennummer')
	ChamBranch=fields.Char('Kanzlei-Niederlassung')
class Felix1TicketKathegories(models.Model):
	_name='felix1.ticket.kathegoriess'
	name=fields.Char('Name')
class ResPartner(models.Model):
	_inherit='res.partner'
	
	ticketing_rel=fields.One2many('felix1.ticket','priPriority') 

