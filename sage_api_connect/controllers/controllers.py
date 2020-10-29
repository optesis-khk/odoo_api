# -*- coding: utf-8 -*-
# from odoo import http


# class SageApiConnect(http.Controller):
#     @http.route('/sage_api_connect/sage_api_connect/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sage_api_connect/sage_api_connect/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sage_api_connect.listing', {
#             'root': '/sage_api_connect/sage_api_connect',
#             'objects': http.request.env['sage_api_connect.sage_api_connect'].search([]),
#         })

#     @http.route('/sage_api_connect/sage_api_connect/objects/<model("sage_api_connect.sage_api_connect"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sage_api_connect.object', {
#             'object': obj
#         })
