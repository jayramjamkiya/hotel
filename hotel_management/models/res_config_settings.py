
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    hotel = fields.Integer(string='hotel')
