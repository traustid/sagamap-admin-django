from django.conf.urls import url
from ..views import (SagaListView, SagaCreateView, SagaDetailView,
                     SagaUpdateView, SagaDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(SagaCreateView.as_view()),
        name="saga_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(SagaUpdateView.as_view()),
        name="saga_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(SagaDeleteView.as_view()),
        name="saga_delete"),

    url(r'^(?P<pk>\d+)/$',
        SagaDetailView.as_view(),
        name="saga_detail"),

    url(r'^$',
        SagaListView.as_view(),
        name="saga_list"),
]
