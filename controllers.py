# -*- coding: utf-8 -*-
from openerp import http

# class ContractExtraInfo(http.Controller):
#     @http.route('/contract_extra_info/contract_extra_info/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contract_extra_info/contract_extra_info/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contract_extra_info.listing', {
#             'root': '/contract_extra_info/contract_extra_info',
#             'objects': http.request.env['contract_extra_info.contract_extra_info'].search([]),
#         })

#     @http.route('/contract_extra_info/contract_extra_info/objects/<model("contract_extra_info.contract_extra_info"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contract_extra_info.object', {
#             'object': obj
#         })