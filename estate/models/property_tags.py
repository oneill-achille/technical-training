from odoo import fields, models


class PropertyTag(models.Model):
    _name = "property.tag"
    _description = "Property Tags"

    name = fields.Char(string="Property Tags")
