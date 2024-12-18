{
    'name': 'Custom Field Service Worksheet',
    'version': '1.0',
    'author': 'Your Name',
    'license': 'AGPL-3',
    'category': 'Field Service',
    'summary': 'Add customizable worksheets and PDF export to Field Service',
    'depends': [
        'field_service',
    ],
    'data': [
        'views/field_service_worksheet_views.xml',
        'report/field_service_worksheet_templates.xml',
    ],
    'installable': True,
    'application': False,
}
