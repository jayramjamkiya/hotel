from odoo.exceptions import ValidationError
from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"


    @api.onchange('tag_ids')
    def test(self):
        print(">>>>>>>>>>\n\n\n>>>>>self",self.name)
        self.client_order_ref = "jayram"

