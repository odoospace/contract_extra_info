# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AccountAnalyticAccount_extra_info(models.Model):
    # _name = 'account.analytic.account'
    _inherit = 'account.analytic.account'
    # _descripton = 'Analytic Account'

    installation_partner_id = fields.Many2one('res.partner', 'Installation Address', select=True, domain="[('parent_id','=', partner_id)]")
 
    imei = fields.Char(string='IMEI', default = "123456789" )
