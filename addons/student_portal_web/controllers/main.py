

from odoo import http
from odoo.http import request

class StudentPortalController(http.Controller):

    @http.route(['/student-portal'], type='http', auth='user', website=True)
    def student_portal(self, **kwargs):
        user = request.env.user
        public_user = request.website.user_id

        if user == public_user:
            return request.redirect('/web/login?redirect=/student-portal')

        is_admin = user.has_group('base.group_system')
        student = request.env['school.student'].sudo().search([('user_id', '=', user.id)], limit=1)
        students = request.env['school.student'].sudo().search([]) if is_admin else None

        return request.render('student_portal_web.student_portal_template', {
            'user': user,
            'student': student,
            'students': students,
            'is_admin': is_admin,
        })

