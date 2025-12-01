# -*- coding: utf-8 -*-
# from odoo import http


# class DcBebidas(http.Controller):
#     @http.route('/dc_bebidas/dc_bebidas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dc_bebidas/dc_bebidas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dc_bebidas.listing', {
#             'root': '/dc_bebidas/dc_bebidas',
#             'objects': http.request.env['dc_bebidas.dc_bebidas'].search([]),
#         })

#     @http.route('/dc_bebidas/dc_bebidas/objects/<model("dc_bebidas.dc_bebidas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dc_bebidas.object', {
#             'object': obj
#         })

