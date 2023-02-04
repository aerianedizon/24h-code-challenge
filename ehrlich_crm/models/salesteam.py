from odoo import api, fields, models

class Salesteams(models.Model):
    _name = 'salesteams'
    _description = 'Sales Teams'

    name = fields.Char('Name')
    contact_id = fields.One2many('opportunities', 'contact_id', string='Customer')

    @api.model
    def create(self, vals):
        res = super(Salesteams, self).create(vals)
        return res

    def write(self, vals):
        res = super(Salesteams, self).write(vals)
        return res
