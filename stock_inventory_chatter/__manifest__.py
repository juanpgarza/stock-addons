# Copyright 2023 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "stock_inventory_chatter",
    "summary": "",
    "version": "15.0.1.0.0",
    "category": "Warehouse Management",
    "website": "https://github.com/juanpgarza/stock-addons",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": 
        ["stock_inventory", # OCA
        ],
    "data": [
        'views/stock_inventory_views.xml',
        ],
    "installable": False,
}