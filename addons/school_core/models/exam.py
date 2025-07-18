from odoo import models, fields

class SchoolExam(models.Model):
    _name = 'school.exam'
    _description = 'Exam'

    name = fields.Char(required=True)
    date = fields.Date()
