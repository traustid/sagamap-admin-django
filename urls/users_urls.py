from django.conf.urls import url
from ..views import (UsersListView, UsersCreateView, UsersDetailView,
                     UsersUpdateView, UsersDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(UsersCreateView.as_view()),
        name="users_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(UsersUpdateView.as_view()),
        name="users_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(UsersDeleteView.as_view()),
        name="users_delete"),

    url(r'^(?P<pk>\d+)/$',
        UsersDetailView.as_view(),
        name="users_detail"),

    url(r'^$',
        UsersListView.as_view(),
        name="users_list"),
]
