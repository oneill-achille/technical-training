from odoo import models, fields

class Estate(models.Model):
    _name = "estate"
    _description = "Estate"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)
    
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The name must be unique.'),
    ]