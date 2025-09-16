{
    "name": "Estate",  # The name that will appear in the App list
    "version": "18.0.0.0.20",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        "security/ir.model.access.csv",
        
        "views/estate_views.xml",
        "views/estate_menu.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
