from odoo import models, fields, api, _
import datetime
from odoo.exceptions import ValidationError


class room(models.Model):
    _name = "room.room"
    _rec_name = "room_number"
    _description = "room"

    room_number = fields.Integer(string='room_number')
    room_type = fields.Selection([('single', 'SINGLE'),
                                  ('double', 'DOUBLE'),
                                  ('dulux', 'DULUX'), ],
                                 index=True, string="room type", required=True)
    facility_ids = fields.Many2many("room.facility", string="facility")
    description = fields.Html(string="description")

    state = fields.Selection([('booked', 'BOOKED'),
                              ('not booked', "NOT BOOKED"), ],
                             index=True, default="not booked", required=True)

    def action_booked(self):
        self.write({'state': 'booked'})
        return True

    def action_not_booked(self):
        self.write({"state": 'not booked'})


class RoomFacility(models.Model):
    _name = "room.facility"
    _rec_name = "facility"
    _description = "facility"

    facility = fields.Char("Facilities")
