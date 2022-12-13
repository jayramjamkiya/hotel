from odoo import api, fields, models


class ReportWizard(models.Model):
    _name = "report.wizard"
    _description = "report"


    start_date = fields.Date(string="start_date", required=True)
    end_date = fields.Date(string="end_date", required=True)

    def print_report(self):
        domain = []

        if self.start_date:
            domain += [('booking_date', '>=', self.start_date)]

        if self.end_date:
            domain += [('booking_date', '<=', self.end_date)]

        booked_history = self.env['booking.booking'].search_read(domain)
        print('------------', booked_history)

        data = {
            'report_start_date': self.read()[0]['start_date'],
            'report_end_date': self.read()[0]['end_date'],
            'booked_history': booked_history
        }

        return self.env.ref('hotel_management.action_report_booking_history').report_action(self, data=data)
