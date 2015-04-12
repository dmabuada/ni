from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('app_plugins.test_app.site.views',
    (r'^$', 'index_page'),
    (r'^admin/', include(admin.site.urls)),
)
