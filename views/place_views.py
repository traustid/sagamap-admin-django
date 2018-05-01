from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Place
from ..forms import PlaceForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class PlaceListView(ListView):
    model = Place
    template_name = "sagamap_admin/place_list.html"
    paginate_by = 20
    context_object_name = "place_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PlaceListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaceListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaceListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PlaceListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PlaceListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PlaceListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PlaceListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PlaceListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PlaceListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PlaceListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceListView, self).get_template_names()


class PlaceDetailView(DetailView):
    model = Place
    template_name = "sagamap_admin/place_detail.html"
    context_object_name = "place"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PlaceDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaceDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaceDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlaceDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlaceDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PlaceDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlaceDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlaceDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceDetailView, self).get_template_names()


class PlaceCreateView(CreateView):
    model = Place
    form_class = PlaceForm
    # fields = ['lat', 'lng', 'name', 'type', 'info', 'info2', 'pkey', 'parish', 'county']
    template_name = "sagamap_admin/place_create.html"
    success_url = reverse_lazy("place_list")

    def __init__(self, **kwargs):
        return super(PlaceCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PlaceCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaceCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlaceCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PlaceCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PlaceCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PlaceCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlaceCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PlaceCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlaceCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlaceCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("place_detail", args=(self.object.pk,))


class PlaceUpdateView(UpdateView):
    model = Place
    form_class = PlaceForm
    # fields = ['lat', 'lng', 'name', 'type', 'info', 'info2', 'pkey', 'parish', 'county']
    template_name = "sagamap_admin/place_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "place"

    def __init__(self, **kwargs):
        return super(PlaceUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaceUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaceUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlaceUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlaceUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlaceUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PlaceUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PlaceUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PlaceUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PlaceUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlaceUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PlaceUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlaceUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlaceUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlaceUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("place_detail", args=(self.object.pk,))


class PlaceDeleteView(DeleteView):
    model = Place
    template_name = "sagamap_admin/place_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "place"

    def __init__(self, **kwargs):
        return super(PlaceDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaceDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PlaceDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PlaceDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlaceDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlaceDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PlaceDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlaceDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlaceDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("place_list")
