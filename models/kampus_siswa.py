from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusSiswa(models.Model):
    _name = 'kampus.siswa'

    name = fields.Char('Name')
    nomor_induk = fields.Char('Nomor Induk', required=True, )
    alamat = fields.Text('Alamat')
    tanggal_masuk = fields.Date(string='Tanggal Masuk', default=fields.Date.today(), )
