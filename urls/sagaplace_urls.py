from django.conf.urls import url
from ..views import (SagaplaceListView, SagaplaceCreateView, SagaplaceDetailView,
                     SagaplaceUpdateView, SagaplaceDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(SagaplaceCreateView.as_view()),
        name="sagaplace_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(SagaplaceUpdateView.as_view()),
        name="sagaplace_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(SagaplaceDeleteView.as_view()),
        name="sagaplace_delete"),

    url(r'^(?P<pk>\d+)/$',
        SagaplaceDetailView.as_view(),
        name="sagaplace_detail"),

    url(r'^$',
        SagaplaceListView.as_view(),
        name="sagaplace_list"),
]
