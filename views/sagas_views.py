from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Sagas
from ..forms import SagasForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class SagasListView(ListView):
    model = Sagas
    template_name = "sagamap_admin/sagas_list.html"
    paginate_by = 20
    context_object_name = "sagas_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SagasListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagasListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagasListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SagasListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SagasListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SagasListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SagasListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SagasListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SagasListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SagasListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SagasListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagasListView, self).get_template_names()


class SagasDetailView(DetailView):
    model = Sagas
    template_name = "sagamap_admin/sagas_detail.html"
    context_object_name = "sagas"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SagasDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagasDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagasDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SagasDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SagasDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SagasDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SagasDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SagasDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SagasDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagasDetailView, self).get_template_names()


class SagasCreateView(CreateView):
    model = Sagas
    form_class = SagasForm
    # fields = ['title', 'info', 'defaultsaga', 'type', 'visible']
    template_name = "sagamap_admin/sagas_create.html"
    success_url = reverse_lazy("sagas_list")

    def __init__(self, **kwargs):
        return super(SagasCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SagasCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagasCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SagasCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SagasCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SagasCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SagasCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SagasCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SagasCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SagasCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SagasCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SagasCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagasCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("sagas_detail", args=(self.object.pk,))


class SagasUpdateView(UpdateView):
    model = Sagas
    form_class = SagasForm
    # fields = ['title', 'info', 'defaultsaga', 'type', 'visible']
    template_name = "sagamap_admin/sagas_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "sagas"

    def __init__(self, **kwargs):
        return super(SagasUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagasUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SagasUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SagasUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SagasUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SagasUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SagasUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SagasUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SagasUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SagasUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SagasUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SagasUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SagasUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SagasUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SagasUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SagasUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagasUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("sagas_detail", args=(self.object.pk,))


class SagasDeleteView(DeleteView):
    model = Sagas
    template_name = "sagamap_admin/sagas_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "sagas"

    def __init__(self, **kwargs):
        return super(SagasDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SagasDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SagasDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SagasDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SagasDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SagasDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SagasDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SagasDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SagasDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SagasDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SagasDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("sagas_list")
