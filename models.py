# -*- coding: utf-8 -*-

from openerp import models, fields, api
from dateutil.relativedelta import relativedelta
from openerp.exceptions import ValidationError

class AccountAnalyticAccount_extra_info(models.Model):
    # _name = 'account.analytic.account'
    _inherit = 'account.analytic.account'
    # _descripton = 'Analytic Account'

    contract_duration_days = fields.Integer(help ="The contract duration (in days)")

    @api.one
    @api.constrains('contract_duration_days')
    def _check_positive_and_not_exagerated_duration(self):
        if self.contract_duration_days < 0:
            raise ValidationError("Duration must be a positive value (or at least zero).")
        
        if self.contract_duration_days > 121:
            raise ValidationError("Duration must be a less than 10 years.")


    @api.onchange('contract_duration_days')
    def calculate_duration(self):
        if not self.date_start:
            self.date_start = fields.date.today()
        
        date_start_dt = fields.Datetime.from_string(self.date_start)
        dt = date_start_dt + relativedelta(days=self.contract_duration_days)
        # new date of contract end is set as initial date plus the contract duration
        self.date = fields.Datetime.to_string(dt)

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
