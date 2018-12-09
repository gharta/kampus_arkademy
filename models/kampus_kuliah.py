from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusKuliah(models.Model):
    _name = 'kampus.kuliah'

    name = fields.Char('Name')
    kapasitas_siswa = fields.Integer(string='Kapasitas Siswa', default=40)
    is_full = fields.Boolean(string='Kelas Penuh ?')
    gender = fields.Selection([
            ('pria', 'Pria'),
            ('wanita', 'Wanita'),
        ], string='Gender',)
