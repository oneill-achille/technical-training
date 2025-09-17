from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_is_zero, float_compare


class Estate(models.Model):
    _name = "estate"
    _description = "Estate"

    # Functions
    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.garden_area + property.living_area

    @api.depends("offers_ids.price")
    def _compute_best_offer(self):
        for property in self:
            if property.offers_ids:
                property.best_offer = max(property.offers_ids.mapped("price"))
            else:
                property.best_offer = 0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = self.garden_orientation = False

    def action_sell_property(self):
        for property in self:
            if property.state == "cancelled":
                raise UserError("Cancelled properties cannot be sold.")

            property.state = "sold"

    def action_cancel_property(self):
        for property in self:
            if property.state == "sold":
                raise UserError("Sold properties cannot be cancelled.")

            property.state = "cancelled"

    @api.constrains("expected_price", "selling_price")
    def _check_prices(self):
        for property in self:
            if not float_is_zero(
                property.selling_price, precision_rounding=0.01
            ) and float_compare(
                property.selling_price,
                property.expected_price * 0.9,
                precision_rounding=0.01,
            ):
                raise ValidationError(
                    "The selling price must be lower than 90% of the expected price."
                )

    # Properties
    name = fields.Char(string="Name", default="Unknown")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(
        string="Date Availability",
        default=lambda self: fields.Date.add(fields.Date.today(), months=3),
    )
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garage Area")
    garden_orientation = fields.Selection(
        [("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")]
    )
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        [
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
        required=True,
        copy=False,
        default="new",
    )
    property_type_id = fields.Many2one("property.type", string="Property Type")
    tags_ids = fields.Many2many("property.tag", string="Tag")
    salesperson_id = fields.Many2one(
        "res.users", string="Salesperson", default=lambda self: self.env.user
    )
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    offers_ids = fields.One2many("offer", "property_id", string="Offers")
    total_area = fields.Integer(compute="_compute_total_area", string="Total Area")
    best_offer = fields.Integer(compute="_compute_best_offer", string="Best Offer")

    # Constraints
    _sql_constraints = [
        (
            "check_expected_price",
            "CHECK(expected_price >= 0)",
            "Expected price must be strictly positive.",
        ),
        (
            "check_selling_price",
            "CHECK(selling_price >= 0)",
            "Selling price must be strictly positive.",
        ),
    ]
