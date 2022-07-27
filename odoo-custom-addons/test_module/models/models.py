# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course_module(models.Model):
    _name = 'customtest.model'

    name = fields.Char()
    id = fields.Integer
    occupation = fields.Char()
    qualification = fields.Char()
    state = fields.Selection([('cart', 'Add to Cart'),
                              ('purchased', 'Purchased'),
                              ('delivered', 'Delivered')], default="cart")


class One_module3(models.Model):

    _inherit = 'account.move'
    occupation = fields.Char()

class One_module4(models.Model):

    _inherit = 'account.move.line'

    field_custom = fields.Char(string="Field for Custom Input")
