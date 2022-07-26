# -*- coding: utf-8 -*-
import string

from odoo import models, fields, api

class One_module1(models.Model):
    _inherit = 'sale.order'

    SalesOnLib = fields.Many2one('customtest.model','id')


class One_module2(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    Customfield = fields.Char()

    # value = f
    # ields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    #
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    # @api.model
    # def create(self, vals_list):
    #     super(One_module1, self).create(vals_list)
    #     print()