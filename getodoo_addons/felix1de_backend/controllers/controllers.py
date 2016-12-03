# -*- coding: utf-8 -*-
from openerp import http

# class Felix1deBackend(http.Controller):
#     @http.route('/felix1de_backend/felix1de_backend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/felix1de_backend/felix1de_backend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('felix1de_backend.listing', {
#             'root': '/felix1de_backend/felix1de_backend',
#             'objects': http.request.env['felix1de_backend.felix1de_backend'].search([]),
#         })

#     @http.route('/felix1de_backend/felix1de_backend/objects/<model("felix1de_backend.felix1de_backend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('felix1de_backend.object', {
#             'object': obj
#         })