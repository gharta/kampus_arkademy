from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusKuliah(models.Model):
    _inherit = 'kampus.kuliah'

    dosen_id = fields.Many2one('kampus.dosen', 'Dosen Terkait')
