# -*- coding: utf-8 -*-

{
    'name': 'Add State field to Project Stages',
    'version': '8.0.1.1.0',
    'category': 'Project Management',
    'summary': 'Restore State attribute removed from Project Stages in 8.0',
    'author': "Daniel Reis,Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/project-service',
    'license': 'AGPL-3',
    'depends': [
        'project',
    ],
    'data': [
        'project_view.xml',
        'project_task_type_data.xml',
        'security/ir.model.access.csv',
        ],
    'installable': True,
}
