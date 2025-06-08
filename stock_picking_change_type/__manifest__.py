# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "stock_picking_change_type",
    "summary": "",
    "version": "17.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/juanpgarza/stock-addons",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": [
            "stock",
            "stock_picking_back2draft",
            ],
    "data": [
        'security/ir.model.access.csv',        
        # 'views/stock_picking_views.xml',        
        'wizards/change_picking_type_views.xml',
        ],
    "installable": False,
}
