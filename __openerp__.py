# -*- coding: utf-8 -*-
{
    'name': "Open Exams",

    'summary': """
        Manage COs and POs and advanced exam management QP genration and Results Analysis""",

    'description': """
        Exam Management adapted for Cochin University of Science and Technology.
        Involves intelligent management of exams and results.
        Maps COs to POs.
        Maps Exams to results.
        Maps Questions to COs.
    """,

    'author': "IT Dept. SOE, Cochin Universiity",
    'website': "http://www.blog.hvinayan.com",
    'category': 'Exam',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True

}
