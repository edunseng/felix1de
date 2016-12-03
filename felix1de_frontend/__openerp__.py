# -*- coding: utf-8 -*-
{
    'name': "felix1.de Kundenportal",

    'summary': """
        felix1.de Webanwendung und Datenbank Frontend""",

    'description': """
        Dieses Modul ersetzt die bisherige MS Access Anwendung.
        Das Kundenportal wurde um die folgende Funktionen erweitert:
        
        - Ticketmanagement (Ticketverwaltung für Manager)
        - Unternehmenskomunikation (intern/extern)
        - Mitarbeiterverwaltung
   """,

    'author': "HiYa Coding LTD",
    'website': "http://www.hiyacoding.co.uk",
    'icon': "/felix1de_frontend/static/description/portal.png",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'felix1.de',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','hr','felix1de_backend','project_issue'],

    # always loaded
    'data': [
        # general view definitions
        'views/views.xml',
        'views/templates.xml',
        # secutŕity
        'security/ir.model.access.csv',
        'security/security.xml',
        # Model related views
        'views/backend.xml',
        'views/res_partner/mandanten.xml',
        ##'views/customer_form_view.xml',
        ##'views/customer_ticketing_view.xml',
        ##'views/branch_view.xml',
        ##'views/contract_view.xml',
        ##'views/bank_details_view.xml',
        ##'views/ticket_employee_view.xml',
        ##'views/order_view.xml',
        ##'views/number_view.xml',
        ##'views/start_ticket.xml',
        ##'views/customer_mail_send_view.xml',
        ##'views/product_view.xml',
        ##'views/mandanten.xml',
        ##'views/kontakte_view.xml',
        ##'views/kanzleien.xml',
        ##'views/project_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': True
}