# -*- coding: utf-8 -*-
{
    'name': "Affectation des positions fiscales et du compte sur la facture - Yziact",

    'summary': """
        Affectation des positions fiscales et du compte sur la facture
    """,

    'description': """
        Affectation des positions fiscales et du compte sur la facture
    """,

    'author': "Yziact",
    'maintainer': 'C. CAPARROS',

    # lien vers le dépôt git ou site Yziact
    'website': "http://gitlab.yziact.net/odoo/commons/module",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Invoicing & Payments',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
        'crm',
        'sales_team',
    ],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    # only loaded in demonstration mode

    'installable': True,
    'application': False,
    'auto_install': False, 

    # Hooks for module installation/uninstallation, their value should be a string
    # representing the name of a function defined inside the module's __init__.py.
    # 'pre_init_hook': '',
    # 'post_init_hook': '',
    # 'uninstall_hook': '',
}

