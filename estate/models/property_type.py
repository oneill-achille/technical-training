from odoo import fields, models


class PropertyType(models.Model):
    _name = "property.type"
    _description = "Property Type"

    name = fields.Char(string="Property Type", required=True)
    property_ids = fields.One2many("estate", "property_type_id", string="Properties")
    title = fields.Char(string="Title")
    expected_price = fields.Float(string="Expected Price")
    status = fields.Selection(
        [
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
    )
