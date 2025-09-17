from odoo import fields, models


class PropertyTag(models.Model):
    _name = "property.tag"
    _description = "Property Tag"
    _order = "name desc"

    name = fields.Char(string="Property Tag")

    # Constraints
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name of the tag must be unique."),
    ]
