# -*- coding: utf-8 -*-
##############################################################################
#
#   ACHIEVE WITHOUT BORDERS
#
##############################################################################
{
    'name': "Ehrlich CRM",

    'summary': """
        Ehrlich CRM
        """,

    'description': """
        Extension Odoo Apps
    """,

    'author': "A. Dizon",

    'license': 'LGPL-3',

    'category': 'Sales/CRM',

    'version': '13.0.1.0.0',

    'depends': [
        'base'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/contacts_view.xml',
        'views/menuitem.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False

}
