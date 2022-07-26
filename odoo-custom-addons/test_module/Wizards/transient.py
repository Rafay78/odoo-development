from odoo import models, fields, api


class CourseTransient_module(models.TransientModel):
    _name = 'Course.Transient'
    _description = 'Course Transient Wizard'

    name = fields.Char('Name')
