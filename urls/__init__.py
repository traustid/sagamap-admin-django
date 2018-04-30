from django.conf.urls import include, url

urlpatterns = [

    url(r'^chapterss/', include('sagamap_admin.urls.chapters_urls')),  # NOQA
    url(r'^placeattrs/', include('sagamap_admin.urls.placeattr_urls')),
    url(r'^placess/', include('sagamap_admin.urls.places_urls')),
    url(r'^sagaplaces/', include('sagamap_admin.urls.sagaplace_urls')),
    url(r'^sagass/', include('sagamap_admin.urls.sagas_urls')),
    url(r'^userss/', include('sagamap_admin.urls.users_urls')),
]
