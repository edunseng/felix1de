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
        # secutŕity
        'security/ir.model.access.csv',
        'security/security.xml',
        'security/ticket_security.xml',
        ## Model related views
        'views/own_menus/backend.xml',
        'views/own_menus/start.xml',
        # project.issue customasations
        'views/project_issue/ticketsystem.xml',
        'views/project_issue/project_view.xml',
         # res.partner customasations
        'views/res_partner/notebooks/bank_details_view.xml',
        #'views/res_partner/mandanten_dlg.xml',
        'views/res_partner/notebooks/order_view.xml',
        'views/res_partner/notebooks/number_view.xml',
        'views/res_partner/notebooks/product_view.xml',
        #'views/res_partner/partner_kontakte.xml',
        'views/res_partner/partner_mandanten.xml',
         # res.company customasations
        'views/res_company/branch_view.xml',        
     
        'views/customer_mail_send_view.xml',
        'views/menu_view.xml',
        
        
        
        
        
        
        
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
    'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': True,
    'qweb': [
        'static/src/xml/client_action.xml',],
    
    
}