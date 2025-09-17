{
    "name": "Estate",
    "version": "18.0.0.0.50",
    "application": True,
    "depends": ["base"],
    "data": [
        # Security
        "security/ir.model.access.csv",
        # Views
        "views/estate_advertisement_views.xml",
        "views/estate_settings_views.xml",
        "views/estate_tags_views.xml",
        "views/estate_offers_views.xml",
        "views/estate_menu.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
