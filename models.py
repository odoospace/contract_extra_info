# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AccountAnalyticAccount_extra_info(models.Model):
    # _name = 'account.analytic.account'
    _inherit = 'account.analytic.account'
    # _descripton = 'Analytic Account'

    installation_partner_id = fields.Many2one('res.partner', 'Installation Address', select=True, domain="[('parent_id','=', partner_id)]")

    # Datos del firmante      
    signer_partner_id   = fields.Many2one('res.partner', "Signer's data", select=True)
    #  Cargo = "Puesto de trabajo"  Nombre: Apellidos:  DNI=NIF

    #Poderes otorgados
    # ante el Notario de       http://www.emiliopolis.net/es/int/geo/nombres_es.htm
    notary_place        = fields.Char(string='Place',size=60)
    #Nombre Notario 
    notary_name         = fields.Char(string='Name of notary', size=50)
    #Nº Protocolo       
    notary_protocol     = fields.Char(string='Protocol',size=40)
    #Fecha Otorgamiento
    notary_date         = fields.Date("Notary's act date")
    #notary_partner_id = fields.Many2one('res.partner', 'Installation Address', select=True)

class Partner_extra_info(models.Model):
    # _name = 'account.analytic.account'
    _inherit = 'res.partner'
    # _descripton = 'Analytic Account'

    notary =  fields.Boolean('Notary', help='check if notary.')
