import app_plugins

register = app_plugins.Library()

def testpoint(point, context, *args, **kwargs):
    'test point'
    return {'var1': 'test'}

register.plugin_point(takes_context=True)(testpoint)