from openerp import models, fields

class AnalyticAccount(models.Model):
    _inherit = 'product.template'
    
    attachments_ids = fields.Many2many('ir.attachment', string="Attachments")