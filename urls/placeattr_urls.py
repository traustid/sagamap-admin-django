from django.conf.urls import url
from ..views import (PlaceattrListView, PlaceattrCreateView, PlaceattrDetailView,
                     PlaceattrUpdateView, PlaceattrDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(PlaceattrCreateView.as_view()),
        name="placeattr_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PlaceattrUpdateView.as_view()),
        name="placeattr_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PlaceattrDeleteView.as_view()),
        name="placeattr_delete"),

    url(r'^(?P<pk>\d+)/$',
        PlaceattrDetailView.as_view(),
        name="placeattr_detail"),

    url(r'^$',
        PlaceattrListView.as_view(),
        name="placeattr_list"),
]
