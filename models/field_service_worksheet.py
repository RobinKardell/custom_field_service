from odoo import models, fields, api

class FieldServiceWorksheet(models.Model):
    _name = 'field.service.worksheet'
    _description = 'Field Service Worksheet'

    name = fields.Char(string="Worksheet Name", required=True, default="New")
    order_id = fields.Many2one(
        'fsm.order', string="Related FSM Order", ondelete='cascade', required=True
    )
    checklist_ids = fields.One2many(
        'field.service.worksheet.checklist', 'worksheet_id', string="Checklist"
    )
    custom_field_ids = fields.One2many(
        'field.service.worksheet.custom_field', 'worksheet_id', string="Custom Fields"
    )
    date = fields.Date(string="Worksheet Date", default=fields.Date.context_today)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string="Status", default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('field.service.worksheet') or 'New'
        return super(FieldServiceWorksheet, self).create(vals)

    def action_start(self):
        self.state = 'in_progress'

    def action_done(self):
        self.state = 'done'


class FieldServiceWorksheetChecklist(models.Model):
    _name = 'field.service.worksheet.checklist'
    _description = 'Worksheet Checklist'

    name = fields.Char(string="Checklist Item", required=True)
    is_done = fields.Boolean(string="Completed", default=False)
    worksheet_id = fields.Many2one(
        'field.service.worksheet', string="Related Worksheet", ondelete='cascade'
    )


class FieldServiceWorksheetCustomField(models.Model):
    _name = 'field.service.worksheet.custom_field'
    _description = 'Custom Field for Worksheet'

    name = fields.Char(string="Field Name", required=True)
    field_type = fields.Selection([
        ('char', 'Text'),
        ('integer', 'Number'),
        ('boolean', 'Checkbox'),
    ], string="Field Type", required=True, default='char')

    value_char = fields.Char(string="Text Value")
    value_integer = fields.Integer(string="Number Value")
    value_boolean = fields.Boolean(string="Checkbox Value")
    worksheet_id = fields.Many2one(
        'field.service.worksheet', string="Related Worksheet", ondelete='cascade'
    )

    @api.onchange('field_type')
    def _clear_values(self):
        self.value_char = False
        self.value_integer = False
        self.value_boolean = False
