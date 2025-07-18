from odoo import models, fields

class SchoolAttendance(models.Model):
    _name = 'school.attendance'
    _description = 'Attendance'

    student_id = fields.Many2one('school.student')
    date = fields.Date()
    status = fields.Selection([('present', 'Present'), ('absent', 'Absent')])
