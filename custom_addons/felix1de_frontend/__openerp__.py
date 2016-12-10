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
    'depends': [        
        'openstow_backend_theme',
        'project_issue','note','board','mail_tracking',
        'base','mail','hr','felix1de_backend','project',
    ],

    # always loaded
    'data': [
        # general view definitions
        'views/views.xml',
        'views/templates.xml',
        # secutŕity
        'security/ir.model.access.csv',
        'security/security.xml',
        'security/ticket_security.xml',
        # Model related views
        'views/own_menus/backend.xml',
        'views/res_partner/partner_kontakte.xml',
        'views/own_menus/start.xml',
        # 'views/res_partner/partner_mandanten.xml',
        #'views/project_issue/ticketsystem.xml',
        #'views/res_company/branch_view.xml',
        #'views/contract_view.xml',
        #'views/res_partner/notebooks/bank_details_view.xml',
        #'security/ticket_security.xml',
        #'views/ticket_employee_view.xml',
        #'views/res_partner/notebooks/order_view.xml',
        #'views/res_partner/notebooks/number_view.xml',
        #'views/customer_mail_send_view.xml',
        #'views/res_partner/notebooks/product_view.xml',
        #'views/mandanten.xml',
        'views/kontakte_view.xml',
        'views/res_company/kanzleien.xml',
        'views/res_partner/notebooks/project_issue/project_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': True
}