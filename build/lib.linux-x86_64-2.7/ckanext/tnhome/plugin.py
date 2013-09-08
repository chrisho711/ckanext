import ckan.plugins as p


def hello_world():
    return 'hello'


class HomePlugin(p.SingletonPlugin):

    p.implements(p.ITemplateHelpers)
    p.implements(p.IConfigurer)
    p.implements(p.IRoutes, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')

    def get_helpers(self):
        return {'hello_world': hello_world}

    def after_map(self, map):
        map.connect('/myhome', controller='ckanext.tnhome.controller.HomeController', action='index')
        return map
