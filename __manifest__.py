# -*- coding: utf-8 -*-
{
    'name': "Custom Project",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Adasfot",
    'website': "http://www.adasoft.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'project', 'pc_project_base', 'pc_invoice_stages'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_sequence_data.xml',
        'views/project_view.xml',
        'views/albaran_project_button.xml',
        'views/albaran_project_view.xml',
        'report/albaran_report_template.xml',
        'report/albaran_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
