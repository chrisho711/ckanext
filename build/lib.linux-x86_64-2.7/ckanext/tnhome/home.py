import ckan.plugins as p



print 'start tnhome'
def hello_world():
    return 'hello'


class HomePlugin(p.SingletonPlugin):

    p.implements(p.ITemplateHelpers)

    def get_helpers(self):
        print 'get_helpers'
        return {'hello_world': hello_world}
