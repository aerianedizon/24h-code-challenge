from odoo import api, fields, models

class Opportunities(models.Model):
    _name = 'opportunities'
    _description = 'Opportunities'

    name = fields.Char('Name')
    contact_id = fields.Many2one('contacts', string='Customer')
    salesteam_id = fields.Many2one('salesteam', string='Sales Team')

    @api.model
    def create(self, vals):
        res = super(Opportunities, self).create(vals)
        return res

    def write(self, vals):
        res = super(Opportunities, self).write(vals)
        return res
