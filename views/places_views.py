from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Places
from ..forms import PlacesForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class PlacesListView(ListView):
    model = Places
    template_name = "sagamap_admin/places_list.html"
    paginate_by = 20
    context_object_name = "places_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PlacesListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlacesListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlacesListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PlacesListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PlacesListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PlacesListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PlacesListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PlacesListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PlacesListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PlacesListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PlacesListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlacesListView, self).get_template_names()


class PlacesDetailView(DetailView):
    model = Places
    template_name = "sagamap_admin/places_detail.html"
    context_object_name = "places"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PlacesDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlacesDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlacesDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlacesDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlacesDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PlacesDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlacesDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlacesDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlacesDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlacesDetailView, self).get_template_names()


class PlacesCreateView(CreateView):
    model = Places
    form_class = PlacesForm
    # fields = ['lat', 'lng', 'name', 'type', 'info', 'info2', 'pkey', 'parish', 'county']
    template_name = "sagamap_admin/places_create.html"
    success_url = reverse_lazy("places_list")

    def __init__(self, **kwargs):
        return super(PlacesCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PlacesCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlacesCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlacesCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PlacesCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PlacesCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PlacesCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlacesCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PlacesCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlacesCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlacesCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PlacesCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlacesCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("places_detail", args=(self.object.pk,))


class PlacesUpdateView(UpdateView):
    model = Places
    form_class = PlacesForm
    # fields = ['lat', 'lng', 'name', 'type', 'info', 'info2', 'pkey', 'parish', 'county']
    template_name = "sagamap_admin/places_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "places"

    def __init__(self, **kwargs):
        return super(PlacesUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlacesUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlacesUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlacesUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlacesUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlacesUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PlacesUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PlacesUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PlacesUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PlacesUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlacesUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PlacesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlacesUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlacesUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlacesUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlacesUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlacesUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("places_detail", args=(self.object.pk,))


class PlacesDeleteView(DeleteView):
    model = Places
    template_name = "sagamap_admin/places_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "places"

    def __init__(self, **kwargs):
        return super(PlacesDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlacesDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PlacesDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PlacesDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlacesDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlacesDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PlacesDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlacesDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlacesDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlacesDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlacesDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("places_list")
