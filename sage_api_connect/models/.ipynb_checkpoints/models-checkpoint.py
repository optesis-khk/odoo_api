-*- coding: utf-8 -*-

from odoo import models, fields, api


class sage_api_connect(models.Model):
    _inherit = 'account.move'
    
    @api.model
    def create(self, vals):
        rec = super(sage_api_connect, self).create(vals)     
        return rec