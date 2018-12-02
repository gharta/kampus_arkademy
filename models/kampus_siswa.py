from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusSiswa(models.Model):
    _name = 'kampus.siswa'

    name = fields.Char('Name')
    nomor_induk = fields.Char('Nomor Induk', required=True, )
    alamat = fields.Text('Alamat')
    tanggal_masuk = fields.Date(string='Tanggal Masuk', default=fields.Date.today(), )

    state = fields.Selection([
            ('aktif', 'Aktif'),
            ('postpone', 'Postpone'),
            ('lulus', 'Lulus'),
        ], string='Status', default='aktif')

    # Data Pribadi
    gender = fields.Selection([
            ('pria', 'Pria'),
            ('wanita', 'Wanita'),
        ], string='Gender',)

    tanggal_lahir = fields.Date(string='Tanggal Lahir', default=fields.Date.today())
