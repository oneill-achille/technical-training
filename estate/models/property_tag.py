from odoo import fields, models


class PropertyTag(models.Model):
    _name = "property.tag"
    _description = "Property Tag"

    name = fields.Char(string="Property Tag")

    # Constraints
    sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name of the tag must be unique."),
    ]
