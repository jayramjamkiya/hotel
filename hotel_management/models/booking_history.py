from odoo import models, fields, api, _


class bookinghistory(models.Model):
    _name = "booking.history"
    _description = "bookinghistory"

    Booking_Reference = fields.Char(default="New", readonly=True)
    customer_name = fields.Char(string="customer name")
    booking_date = fields.Date("booking Date")
    check_in_date = fields.Date("check in date")
    check_out_date = fields.Date("check out date")
    room_type = fields.Selection([('single', 'SINGLE'),
                                  ('double', 'DOUBLE'),
                                  ('delux', 'DELUX'), ],
                                 index=True, string='room type', required=True)
    room_number = fields.Integer(string="room number",
                                 domain="[('room_type', '=', room_type), ('state', '=', 'not booked')]")
