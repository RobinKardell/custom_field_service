{
    'name': 'Field Service Worksheets',
    'version': '1.0',
    'category': 'Field Service',
    'summary': 'Add worksheets to FSM orders',
    'depends': ['fieldservice'],
    'data': [
        'data/sequence.xml',
        'data/field_service_worksheet_data.xml',
        'views/field_service_worksheet_views.xml',
        'views/field_service_worksheet_action.xml',
        'views/field_service_menus.xml',
    ],
    'installable': True,
    'application': False,
}