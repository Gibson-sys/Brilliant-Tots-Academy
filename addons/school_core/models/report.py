from odoo import models, fields

class SchoolReport(models.Model):
    _name = 'school.report'
    _description = 'Report'

    student_id = fields.Many2one('school.student')
    term = fields.Char()
    remarks = fields.Text()
