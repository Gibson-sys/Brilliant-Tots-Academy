from odoo import models, fields

class SchoolHomework(models.Model):
    _name = 'school.homework'
    _description = 'Homework'

    title = fields.Char()
    due_date = fields.Date()
