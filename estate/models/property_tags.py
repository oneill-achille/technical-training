from odoo import fields, models


class PropertyTag(models.Model):
    _name = "property.tags"
    _description = "Property Tags"

    name = fields.Char(string="Property Tags")
