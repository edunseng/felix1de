from openerp import fields,models,api
class client_order(models.Model):
    _name='client.order'
    name=fields.Many2one('res.partner','Mandant')
    client_order_id=fields.Many2one('backend.mandanten','Mandant')
    client_number=fields.Char('Mandantennummer', related='name.client_number')
    date=fields.Date('gebucht am')
    start_date=fields.Date('Start')
    end_date=fields.Date('Ende')
    remarks=fields.Text('Bemerkung')
    state=fields.Selection([('draft','Erstellung'),('new', 'Neu'),('edit','Bearbeitung'),('close', 'Geschlossen'),('cancel', 'Abgebrochen')], string='Status',  default='draft')
    paket_id=fields.Many2one('order.paket')
    paket_amount=fields.Float('Auftragswert', related='paket_id.amount')
    annual_revenue=fields.Float('Jahresumsatz')
    revenue=fields.Float('Einnahmen')
    employee=fields.Char('Arbeitnehmer')
    product_id=fields.One2many('order.product','client_id','Zusatzprodukte')
    price_id=fields.One2many('backend.line', 'order_id', 'Preise')
    
    @api.multi
    def state_new(self):
		self.write({'state':'new'})
    @api.multi
    def state_edit(self):
		self.write({'state':'edit'})
    @api.multi
    def state_close(self):
		self.write({'state':'close'})
    @api.multi
    def state_cancel(self):
		self.write({'state':'cancel'})
  
class order_paket(models.Model):
    _name='order.paket'
    name=fields.Char('Name')
    amount=fields.Float('Auftragswert')
class order_product(models.Model):
    _name='order.product'
    name=fields.Char('Name')
    paket_ids=fields.Many2one('order.paket')
    cur_start_date=fields.Date('Start')
    cur_end_date=fields.Date('Ende')
    cur_remark=fields.Text('Bemerkung')
    client_id=fields.Many2one('client.order')
class client_number(models.Model):
    _name='client.number'
    name=fields.Many2one('res.partner')
    branch_id=fields.Many2one('branch.branch', 'Branch')
    branch_number=fields.Char('Chamber Number', related='branch_id.chamber_number')
    client_number=fields.Char('Client Number', related='name.client_number')
    accountant_id=fields.Many2one('bank.detail', "Steuerberater")
    lohn_agent_no=fields.Char('Lohn-Beraternr.')
    lohn_client_no=fields.Char('Lohn-Mandantennr.')
    name_etl_main_chamber=fields.Char()
    etl_number_main_chmaber=fields.Char()
    valid_from=fields.Date('Gueltig ab')
    valid_until=fields.Date('Gueltig Bis')
    client_history_id=fields.One2many('client.history','client_number_id')
class client_history(models.Model):
    _name='client.history'
    name=fields.Many2one('branch.branch', 'Niederlassung')
    client_number=fields.Char('Mandantennummer')
    client_number_id=fields.Many2one('client.number')
    date_from=fields.Date('Von')
    date_to=fields.Date('Bis')
    
    
