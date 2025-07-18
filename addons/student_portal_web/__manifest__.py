{
    'name': 'Student Portal',
    'version': '1.0',
    'summary': 'Portal access for students to view their profiles',
    'description': 'A module that allows preschool and JHS students to view their profiles via the website portal.',
    'category': 'Education',
    'author': 'Your Name or Company',
    'depends': ['website', 'base'],
    'data': [
        'views/student_portal_template.xml',
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

