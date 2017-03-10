# -*- coding: utf-8 -*-

from openerp import models, fields, api
from dateutil.relativedelta import relativedelta

class AccountAnalyticAccount_extra_info(models.Model):
    # _name = 'account.analytic.account'
    _inherit = 'account.analytic.account'
    # _descripton = 'Analytic Account'

    contract_duration_months = fields.Integer(help ="the contract duracion (in months)")

    @api.onchange('contract_duration_months')
    def new_contract_end_date(self):
        if not self.date_start:
            self.date_start = fields.date.today()
        # remembre: date = contract_end_date
        # self.date = ... 
        
        # in datetime the start date
        date_start_dt = fields.Datetime.from_string(self.date_start)
        # fields.Datetime.from_string(fields.Datetime.now())
        # datetime.datetime(2014, 6, 15, 19, 32, 17)
        # if now = '2014-06-15' 
        dt = date_start_dt + relativedelta(months=self.contract_duration_months)
        self.date = fields.Datetime.to_string(dt)
        pass
    """
    
    """  

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
