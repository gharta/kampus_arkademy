from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusKuliahTopik(models.Model):
    _name = 'kampus.kuliah.topik'

    name = fields.Char('Name')
