{
    'name': 'Field Service Worksheets',
    'version': '1.0',
    'category': 'Field Service',
    'summary': 'Add worksheets to FSM orders',
    'depends': ['fieldservice'],
    'data': [
        'data/sequence.xml',
        'views/field_service_worksheet_views.xml',
        'views/field_service_worksheet_action.xml',
    ],
    'installable': True,
    'application': False,
}