from django.conf.urls import *

from satchmo_store.urls import urlpatterns

from ni import views

urlpatterns += patterns('',
    url(r'^accounts/', include('allauth.urls')),
    url(r'^ping', views.ping, name='health')
)

# if settings.DEBUG:
# import debug_toolbar
#
# # Server statics and uploaded media
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
