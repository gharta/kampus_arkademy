from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusKuliah(models.Model):
    _inherit = 'kampus.kuliah'

    siswa_ids = fields.Many2many('kampus.siswa', string='Siswa Terkait')


# Contoh di Odoo

# A. Super Lengkap
# payment_ids = fields.Many2many('account.payment', 'account_invoice_payment_rel', 'invoice_id', 'payment_id', string="Payments", copy=False, readonly=True)
# invoice_ids = fields.Many2many('account.invoice', 'account_invoice_payment_rel', 'payment_id', 'invoice_id', string="Invoices", copy=False, readonly=True)

# B. Lumayan Lengkap

# tag_ids = fields.Many2many('account.account.tag', 'account_tax_account_tag', string='Tags', help="Optional tags you may want to assign for custom reporting")

# C. Sederhana

# invoice_ids = fields.Many2many('account.invoice', string='Invoices', copy=False)
