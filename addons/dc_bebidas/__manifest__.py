# -*- coding: utf-8 -*-
{
    'name': "Bebidas para Alumnos Daniel Castelao",

    'summary': "Asigna la bebida ideal basada en el nivel de sueño del alumno",

    'description': """
        Módulo para determinar la bebida recomendada para los
        alumnos del Daniel Castelao en función de su nivel de sueño (1-10)
    """,

    'author': "Borja",
    'website': "https://www.danielcastelao.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir.model.access.csv',
        'views/bebidas_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

