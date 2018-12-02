from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusDosen(models.Model):
    _name = 'kampus.dosen'

    name = fields.Char('Name')
