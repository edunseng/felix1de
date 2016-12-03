
{
    'name' : 'Felix1.de WebFrontend',
    'version' : '1.0',
    'author' : 'GetOdoo, HiYACoding LTD',
    'category' : 'Felix1.de WebFrontend',
    'description' : """
Felix1.de WebFrontend Datenbankanwendung
=========================================
Datenbankanwendung zur Verwaltung der Felix1.de Niederlassungen, Mandanten und Kontakte 
und Integrationstool für die Unternehmenslogik.


    """,
    'website': 'http://www.getodoo.com, www.hiyacoding.co.uk',
    'images' : [],
    'depends' : ['base','mail','hr', 'project_issue','felix1de_backend'],
    'data': [
       
        'security/ir.model.access.csv',
        'views/contact.xml',
        'views/customer_form_view.xml',
        'views/customer_ticketing_view.xml',
        'views/branch_view.xml',
        'views/contract_view.xml',
        'views/bank_details_view.xml',
        'security/ticket_security.xml',
        'views/ticket_employee_view.xml',
        'views/order_view.xml',
        'views/number_view.xml',
        'views/start_ticket.xml',
        'views/customer_mail_send_view.xml',
        'views/product_view.xml',
        'views/mandanten.xml',
        'views/kontakte_view.xml',
        'views/kanzleien.xml',
        'views/project_view.xml',
            ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
}
