from datetime import date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class booking(models.Model):
    _name = 'booking.booking'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = "booking"
    _rec_name = "Booking_Reference"

    # onchange in domain
    @api.onchange('Customer_name_id')
    def onchange_Customer_name_id(self):

        # self.example = 'my example'
        for rec in self:
            return {'domain': {'order_id': [('partner_id', '=', rec.Customer_name_id.id)]}}

    Booking_Reference = fields.Char(default="New", readonly=True)
    Check_in_date = fields.Date("Check_in_date", tracking=True)
    Check_out_date = fields.Date("Check_out_date", tracking=True)
    Customer_name_id = fields.Many2one("res.partner", string="Customer name", store=True, tracking=True)
    order_id = fields.Many2one("sale.order", string="sale order")  # sale order mathi lidhe che onchange karel che
    booking_date = fields.Date(string="Booking Date", default=fields.Date.today())
    active = fields.Boolean(string="Active", default=True)
    room_type = fields.Selection([('single', 'SINGLE'),
                                  ('double', 'DOUBLE'),
                                  ('delux', 'DELUX'), ],
                                 index=True, string='room type', required=True)
    room_number_ids = fields.Many2one('room.room', string="room number",
                                      domain="[('room_type', '=', room_type), ('state', '=', 'not booked')]")
    room_facility_ids = fields.Many2many('room.facility', string='room_facility_ids',
                                         related='room_number_ids.facility_ids')
    example = fields.Integer("example", compute='_compute_example_function')

    # ir.cron method in used
    def _my_cron_method(self):
        # cron_id = self.env.ref('calendar.ir_cron_scheduler_alarm').id
        # triggers_before = self.env['ir.cron.trigger'].search([('cron_id', '=', cron_id)])
        # Check_in_date = datetime.today() + relativedelta(months=1, day=1, hours=1)
        # Check_out_date = datetime.today() + relativedelta(months=1, day=1, hours=2)
        print("CRON METHOD CALLED")
        return True

    def _compute_example_function(self):
        print("SSSSSSSSSSSSSSSS", self)
        for rec in self:
            rec.example = 11

    @api.model
    def create(self, vals):
        vals['Booking_Reference'] = self.env['ir.sequence'].next_by_code('booking.booking')
        return super(booking, self).create(vals)

    def book_room(self):
        for rec in self:
            book = rec.room_number_ids
            # book = rec.room_facility_ids
            # print(">>>>>>>>>>>>",book)
            book.action_booked()
            #
            vals = {
                'Booking_Reference': rec.Booking_Reference,
                'customer_name': rec.Customer_name_id.name,
                'check_in_date': rec.Check_in_date,
                'check_out_date': rec.Check_out_date,
                'room_type': rec.room_type,
                'room_number': rec.room_number_ids.room_number,
                'booking_date': rec.booking_date
            }

            self.env['booking.history'].create(vals)

        # -----------------------------------------------------------------------------------------------------------------------
        # (1) write method:-
        # def write(self, vals):
        #     print("________write________", vals)
        #     return super(booking, self).write(vals)

        # (2) create method :-
        # @api.model
        # def create(self, vals):
        #     print(">>>>>>>____create____>>>>>.", vals)
        #     return super(booking, self).create(vals)

        # (3)  copy method :-
        # def copy(self, default=None):
        #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>copy method")
        #     if default is None:
        #         default = {}
        #     if not default.get("address"):
        #         default['address'] = "copy", self.address
        #     return super(booking, self).copy(default)

        # (4) unlink method
        # def unlink(self):
        #     print(">>>>>>>>>>>unlink method.........")
        #     if self.state == 'booked':
        #         raise ValidationError(_("you cannot delete appointment with 'booked' status !"))
        #     return super(booking, self).unlink()

        # (5) search method:-

        # def action_confirm(self):
        #     for recs in self:
        #         patient = self.env['opd.opd'].search([('state', '=', 'draft')])
        #         print(">>>>>>>>>>>>>>>patient............", patient)
        #     for rec in self:
        #         rec.state = 'confirmed'

        # (6) name_get method:-

        # def name_get(self):
        #     result = []
        #     for rec in self:
        #         result.append((
        #             (rec.id, '%s - %s' % (rec.parent_id.name, rec.phone))))
        #         print(">>>>>>>>>>>phone>>>>>>>>>>>>>>>>", result)
        #     return result

        # onchange method :-

        # (7) onchange method ---------------
        # @api.onchange('Customer_name_id')
        # def onchange_name_id(self):
        #     if self.Customer_name_id:
        #         if self.Customer_name_id.booking_date:
        #             self.booking_date = self.Customer_name_id.booking_date
        #         if self.Customer_name_id.example:
        #             self.example = self.Customer_name_id.example
        #         else:
        #             self.booking_date = " "
        #             self.example = " "

        # (8) compute method :-

        # @api.depends('booking_date')
        # def _age_compute(self):
        #     for rec in self:
        #         rec.age = rec.booking_date and date.today().year - rec.booking_date.year or 0

    # what is object
    # what is model
    # what is odoo
    # what is data
    # what is action
    # what is field
    # what is postgresql
    # what is attribute
    # what is O2M
    # what is M2m
    # what is M2O
    # what is wizard
    # what is github
    # what is api
    # what is controller


