from django.conf.urls import url
from ..views import (ChapterListView, ChapterCreateView, ChapterDetailView,
                     ChapterUpdateView, ChapterDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ChapterCreateView.as_view()),
        name="chapter_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ChapterUpdateView.as_view()),
        name="chapter_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ChapterDeleteView.as_view()),
        name="chapter_delete"),

    url(r'^(?P<pk>\d+)/$',
        ChapterDetailView.as_view(),
        name="chapter_detail"),

    url(r'^$',
        ChapterListView.as_view(),
        name="chapter_list"),
]
