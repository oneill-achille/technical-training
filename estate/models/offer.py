from odoo import fields, models


class Offer(models.Model):
    _name = "offer"
    _description = "Offer"

    price = fields.float(string="Price")
    status = fields.Selection(
        [("accepted", "Accepted"), ("refused", "Refused")], string="Status", copy=False
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate", string="Property", required=True)
