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


    def get_kuliah_terkait(self):
        nama_saya = self.name
        kuliah_doc_all = self.env['kampus.kuliah'].search([])
        id_yang_mesti_ditampilin = []
        for dokumen in kuliah_doc_all:
            dokumen_siswa = dokumen.siswa_ids # (kampus.siswa, 2, 3,5)
            nama_siswa = dokumen_siswa.mapped('name') # ['Rezky', 'Tono', 'Dimas ]
            if nama_saya in nama_siswa:
                id_yang_mesti_ditampilin.append(dokumen.id)
        domain = [("id", "in", id_yang_mesti_ditampilin)]
        return {
            'name': 'Enrolled Course',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain' : domain,
            'res_model': 'kampus.kuliah',
            'type': 'ir.actions.act_window',
        }