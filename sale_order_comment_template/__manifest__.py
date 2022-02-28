# Copyright 2019 C2i Change 2 improve - Eduardo Magdalena <emagdalena@c2i.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale Comments",
    "summary": "Comments texts templates on Sale documents",
    "version": "14.0.1.0.0",
    "category": "Sale Management",
    "website": "https://github.com/OCA/stock-logistics-reporting",
    "author": "C2i Change 2 improve," "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["sale", "base_comment_template"],
    "data": [
        "views/sale_order_view.xml",
    ],
    "installable": True,
}
