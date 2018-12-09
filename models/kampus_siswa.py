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

        # """
            # A. Ngambil Objek

            # self.env['kampus.kuliah'] sama seperti

            # Syntax SQL >
            # "FROM kampus_kuliah"
        # """
        tabel_kampus_kuliah = self.env['kampus.kuliah']
        tabel_kampus_siswa = self.env['kampus.siswa']

        # """
            # B. Membaca Satu Dokumen

            # self.env['kampus.kuliah'].browse(1) sama seperti

            # Syntax SQL >
            # "FROM kampus_kuliah WHERE id = 1"
        # """
        kuliah_row_satu = self.env['kampus.kuliah'].browse(1)
        siswa_row_satu = self.env['kampus.siswa'].browse(1)


        # """
            # C. Membaca kolom tertentu pada Satu Dokumen

            # self.env['kampus.kuliah'].browse(1).name sama seperti

            # Syntax SQL >
            # "SELECT name FROM kampus_kuliah WHERE id = 1"
        # """

        kuliah_pertama_name = self.env['kampus.kuliah'].browse(1).name
        siswa_pertama_name = self.env['kampus.siswa'].browse(1).name

        # D. Odoo EMANG baik banget
        # Daripada nulis self.env['kampus.siswa']
        # Langsung aja self
        # Karena memang function ini ada di class KelasSiswa
        
        id_siswa_row_satu = self.browse(1).id
        umur_siswa_row_satu = self.browse(1).umur

        # E. Ketika mencet tombol di Form ID = 15
        id_siswa_row_lima_belas = self.id
        umur_siswa_row_lima_belas = self.umur




        self.env['kampus.kuliah']

        self.env['kampus.kuliah'].browse(1)

        self.env['kampus.kuliah'].browse(1).name
        # self.env['kampus.kuliah'].browse(1).umur
        self.env['kampus.kuliah'].browse(1).dosen_id.id

        # FROM kampus_kuliah

        # FROM kampus_kuliah WHERE id = 1

        # SELECT name FROM kampus_kuliah WHERE id = 1
        # SELECT umur FROM kampus_kuliah WHERE id = 1
        # SELECT dosen_id FROM kampus_kuliah WHERE id = 1


        nama_saya = self.name
        kuliah_doc_all = self.env['kampus.kuliah'].search([])
        id_yang_mesti_ditampilin = []
        for dokumen in kuliah_doc_all:
            dokumen_siswa = dokumen.siswa_ids # (kampus.siswa, 2, 3,5)
            nama_siswa = dokumen_siswa.mapped('name') # ['Rezky', 'Tono', 'Dimas ]
            if nama_saya in nama_siswa:
                id_yang_mesti_ditampilin.append(dokumen.id)
        # Domain
        domain = [("id", "in", id_yang_mesti_ditampilin)]
        # Jurus supaya dari Backend keluarin View Enrolled Course
        return {
            'name': 'Enrolled Course',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain' : domain,
            'res_model': 'kampus.kuliah',
            'type': 'ir.actions.act_window',
        }