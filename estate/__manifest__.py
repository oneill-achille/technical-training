{
    "name": "Estate",  # The name that will appear in the App list
    "version": "18.0.0.0.1",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "license": "LGPL-3",
}
