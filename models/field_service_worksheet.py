from odoo import models, fields

class FieldServiceWorksheet(models.Model):
    _inherit = 'field.service.worksheet'

    checklist_ids = fields.One2many(
        'field.service.worksheet.checklist', 'worksheet_id', string="Checklist"
    )
    custom_field_ids = fields.One2many(
        'field.service.worksheet.custom_field', 'worksheet_id', string="Custom Fields"
    )


class FieldServiceWorksheetChecklist(models.Model):
    _name = 'field.service.worksheet.checklist'
    _description = 'Worksheet Checklist'

    name = fields.Char(string="Item", required=True)
    is_done = fields.Boolean(string="Completed")
    worksheet_id = fields.Many2one('field.service.worksheet', string="Worksheet")


class FieldServiceWorksheetCustomField(models.Model):
    _name = 'field.service.worksheet.custom_field'
    _description = 'Custom Field for Worksheet'

    name = fields.Char(string="Field Name", required=True)
    field_type = fields.Selection([
        ('char', 'Text'),
        ('integer', 'Number'),
        ('boolean', 'Checkbox'),
    ], string="Field Type", required=True)
    value_char = fields.Char(string="Text Value")
    value_integer = fields.Integer(string="Number Value")
    value_boolean = fields.Boolean(string="Checkbox Value")
    worksheet_id = fields.Many2one('field.service.worksheet', string="Worksheet")
