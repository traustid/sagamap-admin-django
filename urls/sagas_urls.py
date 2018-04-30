from django.conf.urls import url
from ..views import (SagasListView, SagasCreateView, SagasDetailView,
                     SagasUpdateView, SagasDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(SagasCreateView.as_view()),
        name="sagas_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(SagasUpdateView.as_view()),
        name="sagas_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(SagasDeleteView.as_view()),
        name="sagas_delete"),

    url(r'^(?P<pk>\d+)/$',
        SagasDetailView.as_view(),
        name="sagas_detail"),

    url(r'^$',
        SagasListView.as_view(),
        name="sagas_list"),
]
