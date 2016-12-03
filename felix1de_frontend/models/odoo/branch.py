from openerp import fields,models,api
class branch_branch(models.Model):
     _name='branch.branch' 
     name=fields.Char('Namenu')
     branch_id=fields.Char('Kanzleien-ID')
     scs_segment=fields.Char()
     chamber_number=fields.Char('Kanzleinummer')#Kanzleiennummer
     etaxre_agent_number=fields.Char('ETAX-Rewe')
     etaxlo_agent_number=fields.Char('ETAX-Lohn')
     etl_name=fields.Char('ETL-Name')
     etl_number=fields.Char('ETL-Nummer')
     remarks=fields.Text('Bemerkungen')#Bemerkungen
     branch_phone=fields.Char('Telefon')#
     branch_email=fields.Char('Email')
     chamber_responsable=fields.Char('Kanzleiverantwortlicher')
     contract_person=fields.Many2one('res.partner', string='Kontaktperson')
     contract_type=fields.Char('Vertragsart')
     differetation=fields.Char('Spezialisierung')
     start_of_contract=fields.Date('Vertragsbeginn')
     cancelation_due=fields.Date('Kuendigung faellig am')
     suspend_on=fields.Date('Ausgesetzt zum')
     suspended_untill=fields.Date('Ausgesetzt bis') 
     ###Relational Fields
     brach_contract_rel=fields.One2many('branch.contract', 'name')
     contact_person_id=fields.One2many('res.partner','branch_rel')
     ######address fields
     branch_street=fields.Char('Str.')
     branch_street_no=fields.Char('Hausnummer')
     branch_street_extra=fields.Char('Str. Extra')
     branch_house_no=fields.Char('Branche Hausnummer')
     branch_post_code=fields.Char('PLZ')
     branch_city=fields.Char('Stadt')
     branch_city_extra=fields.Char('Stadt Extra')
     branch_mail=fields.Char('Email')
    

     
class brach_contract(models.Model):
     _name="branch.contract"
     name=fields.Many2one('branch.branch','Niederlassung Name')
     chamber_id=fields.Char(related='name.branch_id',  string='Niederlassung ID')
     contract_from=fields.Date('Vertragsbegin')
     contract_date=fields.Date('Bertragsstart')
     fee=fields.Float('Preis')
     fee_reduce=fields.Float('Preis Reduziert')
     remark_contract=fields.Text('Bemerkungen zum Vertrag')
     start_contract=fields.Char('Begin')
     cancel_contract=fields.Char('Kuendigung')
     start_reduction=fields.Date('Start Reduzierung')
     end_reduction=fields.Date('Ende Reduzierung')
     contract_type=fields.Char('Vertragsart')
     
class ticket_employee(models.Model):
     _name="ticket.employee"
     name=fields.Char('Vorname')
     last_name=fields.Char('Nachnahme')
     image=fields.Binary()
     emp_short=fields.Char('Abkuerzung')
     emp_mail=fields.Char('Email')
     emp_phone=fields.Char('Telefon')
     emp_editorial=fields.Char('Bemerkung')
     emp_customer_service=fields.Char('Kundenservice')
     emp_distribution=fields.Char('Vertrieb')
     emp_client_list=fields.Many2many('res.partner', 'res_isssd', 'res_idssss')
     
     
