from django.conf.urls import include, url

urlpatterns = [

    url(r'^chapters/', include('sagamap_admin.urls.chapter_urls')),  # NOQA
    url(r'^placeattrs/', include('sagamap_admin.urls.placeattr_urls')),
    url(r'^places/', include('sagamap_admin.urls.place_urls')),
    url(r'^sagaplaces/', include('sagamap_admin.urls.sagaplace_urls')),
    url(r'^sagas/', include('sagamap_admin.urls.saga_urls')),
]
