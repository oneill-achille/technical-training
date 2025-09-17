from odoo import api, fields, models


class Offer(models.Model):
    _name = "offer"
    _description = "Offer"
    _order = "price desc"

    # Functions
    @api.depends("date_deadline", "validity")
    def _compute_date_deadline(self):
        for record in self:
            create_date = record.create_date or fields.Date.today()
            record.date_deadline = fields.Date.add(create_date, days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (
                record.date_deadline - fields.Date.to_date(record.create_date)
            ).days

    def action_accept_offer(self):
        self.status = "accepted"
        for property in self.property_id:
            property.selling_price = self.price

    def action_refuse_offer(self):
        self.status = "refused"

    # Attributes
    price = fields.Float(string="Price")
    status = fields.Selection(
        [("accepted", "Accepted"), ("refused", "Refused")], string="Status", copy=False
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate", string="Property", required=True)
    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(
        string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
    )

    # Constraints
    _sql_constraints = [
        (
            "check_price",
            "CHECK(price > 0)",
            "Price must be strictly positive.",
        ),
    ]
