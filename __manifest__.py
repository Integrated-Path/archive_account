# -*- coding: utf-8 -*-
{
    'name': "Archive Accounts",
    'summary': """This module lets you archive account""",
    'author': "Integrated Path",
    'website': "https://www.int-path.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accoounting',
    'version': '1.0',
     'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],
    # always loaded
    'data': [
        'views/views.xml',
    ],
    'license': 'LGPL-3',
}
