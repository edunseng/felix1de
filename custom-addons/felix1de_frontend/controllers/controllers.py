# -*- coding: utf-8 -*-
from openerp import http

# class Felix1deFrontend(http.Controller):
#     @http.route('/felix1de_frontend/felix1de_frontend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/felix1de_frontend/felix1de_frontend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('felix1de_frontend.listing', {
#             'root': '/felix1de_frontend/felix1de_frontend',
#             'objects': http.request.env['felix1de_frontend.felix1de_frontend'].search([]),
#         })

#     @http.route('/felix1de_frontend/felix1de_frontend/objects/<model("felix1de_frontend.felix1de_frontend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('felix1de_frontend.object', {
#             'object': obj
#         })