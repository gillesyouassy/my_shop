# -*- coding: utf-8 -*-
{
    'name': "YGABEST-FAHION",

    'summary': """
        Habillez vous comme des Stars, la vie est trop courte pour s"habiller triste
        """,

    'description': """
        Maison D'habillement et de chaussures
    """,

    'author': "Youassy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme/Creative',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/assets.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}