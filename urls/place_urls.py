from django.conf.urls import url
from ..views import (PlaceListView, PlaceCreateView, PlaceDetailView,
                     PlaceUpdateView, PlaceDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(PlaceCreateView.as_view()),
        name="place_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PlaceUpdateView.as_view()),
        name="place_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PlaceDeleteView.as_view()),
        name="place_delete"),

    url(r'^(?P<pk>\d+)/$',
        PlaceDetailView.as_view(),
        name="place_detail"),

    url(r'^$',
        PlaceListView.as_view(),
        name="place_list"),
]
