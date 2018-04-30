from django.conf.urls import url
from ..views import (PlacesListView, PlacesCreateView, PlacesDetailView,
                     PlacesUpdateView, PlacesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(PlacesCreateView.as_view()),
        name="places_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PlacesUpdateView.as_view()),
        name="places_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PlacesDeleteView.as_view()),
        name="places_delete"),

    url(r'^(?P<pk>\d+)/$',
        PlacesDetailView.as_view(),
        name="places_detail"),

    url(r'^$',
        PlacesListView.as_view(),
        name="places_list"),
]
