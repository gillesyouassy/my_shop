from odoo import http
from odoo.addons.portal.controllers.web import Home
from odoo.http import request


class MyShop(Home):
    @http.route()
    def index(self, **kw):
        super(MyShop, self).index()
        return request.render("website.homepage")