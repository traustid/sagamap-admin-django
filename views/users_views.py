from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Users
from ..forms import UsersForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class UsersListView(ListView):
    model = Users
    template_name = "sagamap_admin/users_list.html"
    paginate_by = 20
    context_object_name = "users_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(UsersListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(UsersListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(UsersListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(UsersListView, self).get_queryset()

    def get_allow_empty(self):
        return super(UsersListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(UsersListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(UsersListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(UsersListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(UsersListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(UsersListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(UsersListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(UsersListView, self).get_template_names()


class UsersDetailView(DetailView):
    model = Users
    template_name = "sagamap_admin/users_detail.html"
    context_object_name = "users"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(UsersDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(UsersDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(UsersDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(UsersDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(UsersDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(UsersDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(UsersDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(UsersDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(UsersDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(UsersDetailView, self).get_template_names()


class UsersCreateView(CreateView):
    model = Users
    form_class = UsersForm
    # fields = ['uname', 'name', 'pass_field', 'type']
    template_name = "sagamap_admin/users_create.html"
    success_url = reverse_lazy("users_list")

    def __init__(self, **kwargs):
        return super(UsersCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(UsersCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(UsersCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(UsersCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(UsersCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(UsersCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(UsersCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(UsersCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(UsersCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(UsersCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(UsersCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(UsersCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(UsersCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("users_detail", args=(self.object.pk,))


class UsersUpdateView(UpdateView):
    model = Users
    form_class = UsersForm
    # fields = ['uname', 'name', 'pass_field', 'type']
    template_name = "sagamap_admin/users_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "users"

    def __init__(self, **kwargs):
        return super(UsersUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(UsersUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(UsersUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(UsersUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(UsersUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(UsersUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(UsersUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(UsersUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(UsersUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(UsersUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(UsersUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(UsersUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(UsersUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(UsersUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(UsersUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(UsersUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(UsersUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("users_detail", args=(self.object.pk,))


class UsersDeleteView(DeleteView):
    model = Users
    template_name = "sagamap_admin/users_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "users"

    def __init__(self, **kwargs):
        return super(UsersDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(UsersDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(UsersDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(UsersDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(UsersDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(UsersDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(UsersDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(UsersDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(UsersDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(UsersDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(UsersDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("users_list")
