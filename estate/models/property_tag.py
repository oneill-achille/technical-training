from odoo import fields, models


class PropertyTags(models.Model):
    _name = "property.tag"
    _description = "Property Tag"

    name = fields.Char(string="Property Tag")
