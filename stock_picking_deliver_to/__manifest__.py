# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "stock_picking_deliver_to",
    "summary": "",
    "version": "15.0.2.0.0",
    "category": "Warehouse Management",
    "website": "https://github.com/juanpgarza/stock-addons",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": 
        [
            "stock",
        ],
    "data": [
        'views/stock_picking_views.xml',
        'views/report_deliveryslip.xml',
        ],
    "installable": False,
}