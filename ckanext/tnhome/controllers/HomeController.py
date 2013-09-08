import ckan.lib.base as base
import ckan.plugins as p


class HomeController(base.BaseController):

    def index(self):
        return p.toolkit.render('home/index.html')
