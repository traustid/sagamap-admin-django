from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Chapters
from ..forms import ChaptersForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class ChaptersListView(ListView):
    model = Chapters
    template_name = "sagamap_admin/chapters_list.html"
    paginate_by = 20
    context_object_name = "chapters_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ChaptersListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ChaptersListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ChaptersListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ChaptersListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ChaptersListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ChaptersListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ChaptersListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ChaptersListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ChaptersListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ChaptersListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ChaptersListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChaptersListView, self).get_template_names()


class ChaptersDetailView(DetailView):
    model = Chapters
    template_name = "sagamap_admin/chapters_detail.html"
    context_object_name = "chapters"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ChaptersDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ChaptersDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ChaptersDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ChaptersDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ChaptersDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ChaptersDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ChaptersDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ChaptersDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ChaptersDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChaptersDetailView, self).get_template_names()


class ChaptersCreateView(CreateView):
    model = Chapters
    form_class = ChaptersForm
    # fields = ['title', 'chapter', 'text', 'saga']
    template_name = "sagamap_admin/chapters_create.html"
    success_url = reverse_lazy("chapters_list")

    def __init__(self, **kwargs):
        return super(ChaptersCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ChaptersCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ChaptersCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ChaptersCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ChaptersCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ChaptersCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ChaptersCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ChaptersCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ChaptersCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ChaptersCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ChaptersCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ChaptersCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChaptersCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("chapters_detail", args=(self.object.pk,))


class ChaptersUpdateView(UpdateView):
    model = Chapters
    form_class = ChaptersForm
    # fields = ['title', 'chapter', 'text', 'saga']
    template_name = "sagamap_admin/chapters_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "chapters"

    def __init__(self, **kwargs):
        return super(ChaptersUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ChaptersUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ChaptersUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ChaptersUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ChaptersUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ChaptersUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ChaptersUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ChaptersUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ChaptersUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ChaptersUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ChaptersUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ChaptersUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ChaptersUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ChaptersUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ChaptersUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ChaptersUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChaptersUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("chapters_detail", args=(self.object.pk,))


class ChaptersDeleteView(DeleteView):
    model = Chapters
    template_name = "sagamap_admin/chapters_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "chapters"

    def __init__(self, **kwargs):
        return super(ChaptersDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ChaptersDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ChaptersDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ChaptersDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ChaptersDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ChaptersDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ChaptersDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ChaptersDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ChaptersDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ChaptersDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChaptersDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("chapters_list")
