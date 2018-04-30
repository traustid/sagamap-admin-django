from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Placeattr
from ..forms import PlaceattrForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class PlaceattrListView(ListView):
    model = Placeattr
    template_name = "sagamap_admin/placeattr_list.html"
    paginate_by = 20
    context_object_name = "placeattr_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PlaceattrListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaceattrListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaceattrListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PlaceattrListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PlaceattrListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PlaceattrListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PlaceattrListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PlaceattrListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PlaceattrListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PlaceattrListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceattrListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceattrListView, self).get_template_names()


class PlaceattrDetailView(DetailView):
    model = Placeattr
    template_name = "sagamap_admin/placeattr_detail.html"
    context_object_name = "placeattr"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PlaceattrDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaceattrDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaceattrDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlaceattrDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlaceattrDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PlaceattrDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlaceattrDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlaceattrDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceattrDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceattrDetailView, self).get_template_names()


class PlaceattrCreateView(CreateView):
    model = Placeattr
    form_class = PlaceattrForm
    # fields = ['type', 'place', 'attr1', 'attr2']
    template_name = "sagamap_admin/placeattr_create.html"
    success_url = reverse_lazy("placeattr_list")

    def __init__(self, **kwargs):
        return super(PlaceattrCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PlaceattrCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaceattrCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlaceattrCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PlaceattrCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PlaceattrCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PlaceattrCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlaceattrCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PlaceattrCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlaceattrCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlaceattrCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceattrCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceattrCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("placeattr_detail", args=(self.object.pk,))


class PlaceattrUpdateView(UpdateView):
    model = Placeattr
    form_class = PlaceattrForm
    # fields = ['type', 'place', 'attr1', 'attr2']
    template_name = "sagamap_admin/placeattr_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "placeattr"

    def __init__(self, **kwargs):
        return super(PlaceattrUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaceattrUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PlaceattrUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PlaceattrUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlaceattrUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlaceattrUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PlaceattrUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PlaceattrUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PlaceattrUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PlaceattrUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PlaceattrUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PlaceattrUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PlaceattrUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PlaceattrUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlaceattrUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceattrUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceattrUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("placeattr_detail", args=(self.object.pk,))


class PlaceattrDeleteView(DeleteView):
    model = Placeattr
    template_name = "sagamap_admin/placeattr_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "placeattr"

    def __init__(self, **kwargs):
        return super(PlaceattrDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PlaceattrDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PlaceattrDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PlaceattrDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PlaceattrDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PlaceattrDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PlaceattrDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PlaceattrDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PlaceattrDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PlaceattrDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PlaceattrDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("placeattr_list")
