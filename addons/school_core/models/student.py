from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(required=True)
    age = fields.Integer()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
