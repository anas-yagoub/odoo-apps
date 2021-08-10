# -*- coding: utf-8 -*-
{
    'name': "Spare Project",
    'summary': """
    هذاالنظام يمكنك بكل سهولة من إدارة محلك التجاري بإستخدام مديول حسابات عالية الكفاءة
        """,
    'description': """
        Long description of module's purpose
    """,
    'author': "Julia Mousa , Anas Yagoub",
    'website': "http://www.smartsnode.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','om_account_accountant','account','low','hr_contract'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/payment.xml',
        'data/sequence.xml',
        'views/views.xml',
        'views/account_move.xml',
        'views/analytic_account.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,

}