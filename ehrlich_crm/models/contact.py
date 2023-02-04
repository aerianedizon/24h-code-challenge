from odoo import api, fields, models

class Contacts(models.Model):
    _name = 'contacts'
    _description = 'Contacts'

    name = fields.Char('Name')
    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    street = fields.Char('Street Address')
    barangay = fields.Char('Barangay')
    city = fields.Char('City/Municipality')
    province = fields.Char('Province')
    zip_code = fields.Integer('Zip Code')
    email = fields.Char('Email Address')
    phone = fields.Char('Mobile Number')
    company = fields.Char('Company')
    job_title = fields.Char('Job Title')
    notes = fields.Char('Notes')

    @api.model
    def create(self, vals):
        vals['name'] =  vals['first_name'] + " " +vals['last_name']
        res = super(Contacts, self).create(vals)
        return res

    def write(self, vals):
        res = super(Contacts, self).write(vals)
        return res
