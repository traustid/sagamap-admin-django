from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Saga
from ..forms import SagaForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class SagaListView(ListView):
    model = Saga
    template_name = "sagamap_admin/saga_list.html"
    paginate_by = 20
    context_object_name = "saga_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SagaListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagaListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SagaListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SagaListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SagaListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SagaListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SagaListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SagaListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SagaListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SagaListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaListView, self).get_template_names()


class SagaDetailView(DetailView):
    model = Saga
    template_name = "sagamap_admin/saga_detail.html"
    context_object_name = "saga"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SagaDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagaDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagaDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SagaDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SagaDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SagaDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SagaDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SagaDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SagaDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaDetailView, self).get_template_names()


class SagaCreateView(CreateView):
    model = Saga
    form_class = SagaForm
    # fields = ['title', 'info', 'defaultsaga', 'type', 'visible']
    template_name = "sagamap_admin/saga_create.html"
    success_url = reverse_lazy("saga_list")

    def __init__(self, **kwargs):
        return super(SagaCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SagaCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagaCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SagaCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SagaCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SagaCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SagaCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SagaCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SagaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SagaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SagaCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SagaCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("saga_detail", args=(self.object.pk,))


class SagaUpdateView(UpdateView):
    model = Saga
    form_class = SagaForm
    # fields = ['title', 'info', 'defaultsaga', 'type', 'visible']
    template_name = "sagamap_admin/saga_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "saga"

    def __init__(self, **kwargs):
        return super(SagaUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagaUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagaUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SagaUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SagaUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SagaUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SagaUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SagaUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SagaUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SagaUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SagaUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SagaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SagaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SagaUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SagaUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SagaUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("saga_detail", args=(self.object.pk,))


class SagaDeleteView(DeleteView):
    model = Saga
    template_name = "sagamap_admin/saga_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "saga"

    def __init__(self, **kwargs):
        return super(SagaDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagaDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SagaDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SagaDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SagaDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SagaDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SagaDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SagaDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SagaDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SagaDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagaDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("saga_list")
