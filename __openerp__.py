# -*- coding: utf-8 -*-
{
    'name': "contract_extra_info",

    'summary': """
        Add informations to the contract""",

    'description': """
        Informations like installation address, notary reference...
    """,

    'author': "Impulzia",
    'website': "http://www.odoo.space",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
    'account_analytic_analysis',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}