# -*- coding: utf-8 -*-
# from odoo import http


# class Zinfogtask(http.Controller):
#     @http.route('/zinfogtask/zinfogtask', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zinfogtask/zinfogtask/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zinfogtask.listing', {
#             'root': '/zinfogtask/zinfogtask',
#             'objects': http.request.env['zinfogtask.zinfogtask'].search([]),
#         })

#     @http.route('/zinfogtask/zinfogtask/objects/<model("zinfogtask.zinfogtask"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zinfogtask.object', {
#             'object': obj
#         })
