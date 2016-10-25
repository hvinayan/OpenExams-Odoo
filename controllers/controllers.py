# -*- coding: utf-8 -*-
from openerp import http

# class Openexams(http.Controller):
#     @http.route('/openexams/openexams/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openexams/openexams/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openexams.listing', {
#             'root': '/openexams/openexams',
#             'objects': http.request.env['openexams.openexams'].search([]),
#         })

#     @http.route('/openexams/openexams/objects/<model("openexams.openexams"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openexams.object', {
#             'object': obj
#         })
