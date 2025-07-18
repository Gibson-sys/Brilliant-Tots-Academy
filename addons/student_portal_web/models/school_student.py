from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student Profile'

    name = fields.Char(string='Name', required=True)
    student_id = fields.Char(string='Student ID', required=True)
    user_id = fields.Many2one('res.users', string='Related User')
