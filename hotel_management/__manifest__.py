{
    'name': 'Hotel Management',
    'sequence': -100,
    'version': '1.0.0',

    'depends': ['base', 'sale', 'mail'],
    'description': """
    """,
    'data': [
        'security/ir.model.access.csv',
        'wizard/report_wizard.xml',
        'views/hotel_menu.xml',
        'views/booking.xml',
        'views/booking_history.xml',
        'views/room.xml',
        # 'views/res_config_settings_views.xml',  # setting ma (sale) ni jem hotel nu module add thay 6 ...
        'report/booking_template.xml',
        'report/booking_report.xml',
    ],
    'demo': [

    ],
    'application': True,
    'license': 'LGPL-3',
}
