from odoo import models, fields, api, _


class FieldServiceWorksheet(models.Model):
    _name = 'field.service.worksheet'
    _description = 'Field Service Worksheet'

    name = fields.Char(
        string="Worksheet Name", required=True, default="New", copy=False
    )
    order_id = fields.Many2one(
        'fsm.order', string="Related FSM Order", ondelete='cascade', required=True
    )
    checklist_ids = fields.One2many(
        'field.service.worksheet.checklist', 'worksheet_id', string="Checklist"
    )
    custom_field_ids = fields.One2many(
        'field.service.worksheet.custom_field', 'worksheet_id', string="Custom Fields"
    )
    date = fields.Date(
        string="Worksheet Date", default=fields.Date.context_today, required=True
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
        ],
        string="Status",
        default='draft',
        required=True,
    )

    @api.model
    def create(self, vals):
        """Override the create method to set a unique name using a sequence."""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'field.service.worksheet'
            ) or _('New')
        return super().create(vals)

    def action_start(self):
        """Mark the worksheet as 'In Progress'."""
        for record in self:
            record.state = 'in_progress'

    def action_done(self):
        """Mark the worksheet as 'Done'."""
        for record in self:
            record.state = 'done'


class FieldServiceWorksheetChecklist(models.Model):
    _name = 'field.service.worksheet.checklist'
    _description = 'Worksheet Checklist'

    name = fields.Char(
        string="Checklist Item", required=True, help="Description of the checklist item"
    )
    is_done = fields.Boolean(
        string="Completed", default=False, help="Mark this item as completed"
    )
    worksheet_id = fields.Many2one(
        'field.service.worksheet',
        string="Related Worksheet",
        ondelete='cascade',
        required=True,
    )


class FieldServiceWorksheetCustomField(models.Model):
    _name = 'field.service.worksheet.custom_field'
    _description = 'Custom Field for Worksheet'

    name = fields.Char(
        string="Field Name",
        required=True,
        help="Name of the custom field (e.g., 'Serial Number')",
    )
    field_type = fields.Selection(
        [
            ('char', 'Text'),
            ('integer', 'Number'),
            ('boolean', 'Checkbox'),
        ],
        string="Field Type",
        required=True,
        default='char',
        help="Type of the custom field",
    )
    value_char = fields.Char(
        string="Text Value", help="Value for text fields"
    )
    value_integer = fields.Integer(
        string="Number Value", help="Value for numeric fields"
    )
    value_boolean = fields.Boolean(
        string="Checkbox Value", help="Value for checkbox fields"
    )
    worksheet_id = fields.Many2one(
        'field.service.worksheet',
        string="Related Worksheet",
        ondelete='cascade',
        required=True,
    )

    @api.onchange('field_type')
    def _clear_values(self):
        """Clear irrelevant field values when changing the field type."""
        self.value_char = False
        self.value_integer = False
        self.value_boolean = False
