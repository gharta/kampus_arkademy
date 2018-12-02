from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusSiswa(models.Model):
    _name = 'kampus.siswa'

    name = fields.Char('Name')
