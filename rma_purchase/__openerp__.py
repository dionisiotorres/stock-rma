# -*- coding: utf-8 -*-
# Copyright 2017-18 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)
{
    'name': 'RMA Purchase',
    'version': '9.0.2.0.0',
    'category': 'RMA',
    'summary': 'RMA from PO',
    'license': 'LGPL-3',
    'author': 'Eficent, Odoo Community Association (OCA)',
    'website': 'http://www.github.com/OCA/rma',
    'depends': ['rma_account', 'purchase'],
    'data': [
        'views/rma_operation_view.xml',
        'views/rma_order_view.xml',
        'views/rma_order_line_view.xml',
        'wizards/rma_add_purchase.xml',
    ],
    'installable': True,
    'auto_install': True,
    "post_init_hook": "post_init_hook",
}
