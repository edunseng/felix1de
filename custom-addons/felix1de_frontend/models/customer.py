# -*- coding: utf-8 -*-
from openerp import fields,models,api,_


class ContactContacts(models.Model):
	#_name='contact.contacts'
	_inherit='res.partner' 
	_inherits={'backend.kontakte':'backendkontakt_id'}
	backendkontakt_id=fields.Many2one('backend.kontakte', required=True, ondelete='cascade', index=True)
	
	image=fields.Binary(String="image")
	#name=fields.Char('Name des Mandanten', invisible=True)
	last_name=fields.Char('last name')
	contact_id=fields.Char('Contact ID')
	con_acquired_by=fields.Char('Acquired By')
	contact_since=fields.Char('Kontakt seit')
	phone=fields.Char('phone')
	mobile=fields.Char('mobile')
	fax=fields.Char('fax')
	email=fields.Char('email')
	comment=fields.Char('comment')
	title=fields.Char('title')
	house_no=fields.Char('house_no')
	street=fields.Char('street')
	street2=fields.Char('street2')
	zip=fields.Char('zip')
	city=fields.Char('city')
	state=fields.Char('state')
	kontakt_seit=fields.Date('Kontakt Seit')
	country_id=fields.Many2one('res.country')
	ticket_id=fields.One2many('felix1.ticket', 'contact_id')
	client_id=fields.One2many('res.partner', 'contact_id')

