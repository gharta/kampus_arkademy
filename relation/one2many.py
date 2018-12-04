from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusKuliahTopik(models.Model):
    _inherit = 'kampus.kuliah.topik'

    kampus_id = fields.Many2one('kampus.kuliah', 'Kuliah Terkait')


class KampusKuliah(models.Model):
    _inherit = 'kampus.kuliah'

    topik_ids = fields.One2many('kampus.kuliah.topik', 'kampus_id', 'Line')
