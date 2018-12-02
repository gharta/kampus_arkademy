from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusKuliah(models.Model):
    _name = 'kampus.kuliah'

    name = fields.Char('Name')
