from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Sagaplace
from ..forms import SagaplaceForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class SagaplaceListView(ListView):
    model = Sagaplace
    template_name = "sagamap_admin/sagaplace_list.html"
    paginate_by = 20
    context_object_name = "sagaplace_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SagaplaceListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagaplaceListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagaplaceListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SagaplaceListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SagaplaceListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SagaplaceListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SagaplaceListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SagaplaceListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SagaplaceListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SagaplaceListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SagaplaceListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaplaceListView, self).get_template_names()


class SagaplaceDetailView(DetailView):
    model = Sagaplace
    template_name = "sagamap_admin/sagaplace_detail.html"
    context_object_name = "sagaplace"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SagaplaceDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagaplaceDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagaplaceDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SagaplaceDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SagaplaceDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SagaplaceDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SagaplaceDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SagaplaceDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SagaplaceDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaplaceDetailView, self).get_template_names()


class SagaplaceCreateView(CreateView):
    model = Sagaplace
    form_class = SagaplaceForm
    # fields = ['place', 'saga', 'chapter']
    template_name = "sagamap_admin/sagaplace_create.html"
    success_url = reverse_lazy("sagaplace_list")

    def __init__(self, **kwargs):
        return super(SagaplaceCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SagaplaceCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagaplaceCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SagaplaceCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SagaplaceCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SagaplaceCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SagaplaceCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SagaplaceCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SagaplaceCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SagaplaceCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SagaplaceCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SagaplaceCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaplaceCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("sagaplace_detail", args=(self.object.pk,))


class SagaplaceUpdateView(UpdateView):
    model = Sagaplace
    form_class = SagaplaceForm
    # fields = ['place', 'saga', 'chapter']
    template_name = "sagamap_admin/sagaplace_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "sagaplace"

    def __init__(self, **kwargs):
        return super(SagaplaceUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagaplaceUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagaplaceUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SagaplaceUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SagaplaceUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SagaplaceUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SagaplaceUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SagaplaceUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SagaplaceUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SagaplaceUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SagaplaceUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SagaplaceUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SagaplaceUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SagaplaceUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SagaplaceUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SagaplaceUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaplaceUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("sagaplace_detail", args=(self.object.pk,))


class SagaplaceDeleteView(DeleteView):
    model = Sagaplace
    template_name = "sagamap_admin/sagaplace_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "sagaplace"

    def __init__(self, **kwargs):
        return super(SagaplaceDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagaplaceDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SagaplaceDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SagaplaceDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SagaplaceDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SagaplaceDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SagaplaceDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SagaplaceDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SagaplaceDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SagaplaceDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaplaceDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("sagaplace_list")
