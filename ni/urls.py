from django.conf.urls import patterns, include, url

# staticfiles testing
# from django.conf.urls.static import static
# from django.conf import settings

from satchmo_store.urls import urlpatterns


from ni import views

urlpatterns = patterns('',
    url(r'^accounts/', include('allauth.urls')),
    url(r'^ping', views.ping, name='health'),
    url(r'^search/', views.search.search_view, name='ni-search')
) + urlpatterns

# if settings.DEBUG:
# import debug_toolbar
#
# # Server statics and uploaded media
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += [
#     url(r'^__debug__/', include(debug_toolbar.urls)),
# ]
