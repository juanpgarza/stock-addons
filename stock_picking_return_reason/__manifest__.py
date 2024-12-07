# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "stock_picking_return_reason",
    "summary": "",
    "version": "15.0.1.0.0",
    "category": "Warehouse Management",
    "website": "https://github.com/juanpgarza/stock-addons",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": 
        ["stock",
        # Para ocultar el campo reason (adhoc)
        "stock_ux",
        ],
    "data": [
        'views/stock_picking_views.xml',
        'views/stock_return_picking_reason_views.xml',
        'wizards/stock_return_picking_views.xml',
        'security/ir.model.access.csv',
        ],
    "installable": False,
}