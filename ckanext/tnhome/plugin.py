import ckan.plugins as p


def hello_world():
    return 'hello'


def hot_datasource():
    return p.toolkit.render_snippet('home/snippets/hot_datasource.html')


def lastest_datasource():
    return p.toolkit.render_snippet('home/snippets/lastest_datasource.html')


class HomePlugin(p.SingletonPlugin):

    p.implements(p.ITemplateHelpers)
    p.implements(p.IConfigurer)
    p.implements(p.IRoutes, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'theme/templates')
        p.toolkit.add_public_directory(config, 'theme/public')

    def get_helpers(self):
        return {'hello_world': hello_world, 'hot_datasource': hot_datasource, 'lastest_datasource': lastest_datasource}

    def after_map(self, map):
        map.connect('/myhome', controller='ckanext.tnhome.controllers.HomeController:HomeController', action='index')
        return map
