from django.conf.urls import url
from ..views import (ChaptersListView, ChaptersCreateView, ChaptersDetailView,
                     ChaptersUpdateView, ChaptersDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ChaptersCreateView.as_view()),
        name="chapters_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ChaptersUpdateView.as_view()),
        name="chapters_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ChaptersDeleteView.as_view()),
        name="chapters_delete"),

    url(r'^(?P<pk>\d+)/$',
        ChaptersDetailView.as_view(),
        name="chapters_detail"),

    url(r'^$',
        ChaptersListView.as_view(),
        name="chapters_list"),
]
