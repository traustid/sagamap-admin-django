from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Chapter
from ..forms import ChapterForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class ChapterListView(ListView):
    model = Chapter
    template_name = "sagamap_admin/chapter_list.html"
    paginate_by = 20
    context_object_name = "chapter_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ChapterListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ChapterListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ChapterListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ChapterListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ChapterListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ChapterListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ChapterListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ChapterListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ChapterListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ChapterListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ChapterListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChapterListView, self).get_template_names()


class ChapterDetailView(DetailView):
    model = Chapter
    template_name = "sagamap_admin/chapter_detail.html"
    context_object_name = "chapter"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ChapterDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ChapterDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ChapterDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ChapterDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ChapterDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ChapterDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ChapterDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ChapterDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ChapterDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChapterDetailView, self).get_template_names()


class ChapterCreateView(CreateView):
    model = Chapter
    form_class = ChapterForm
    # fields = ['title', 'chapter', 'text', 'saga']
    template_name = "sagamap_admin/chapter_create.html"
    success_url = reverse_lazy("chapter_list")

    def __init__(self, **kwargs):
        return super(ChapterCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ChapterCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ChapterCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ChapterCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ChapterCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ChapterCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ChapterCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ChapterCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ChapterCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ChapterCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ChapterCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ChapterCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChapterCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("chapter_detail", args=(self.object.pk,))


class ChapterUpdateView(UpdateView):
    model = Chapter
    form_class = ChapterForm
    # fields = ['title', 'chapter', 'text', 'saga']
    template_name = "sagamap_admin/chapter_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "chapter"

    def __init__(self, **kwargs):
        return super(ChapterUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ChapterUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ChapterUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ChapterUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ChapterUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ChapterUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ChapterUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ChapterUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ChapterUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ChapterUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ChapterUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ChapterUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ChapterUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ChapterUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ChapterUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ChapterUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChapterUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("chapter_detail", args=(self.object.pk,))


class ChapterDeleteView(DeleteView):
    model = Chapter
    template_name = "sagamap_admin/chapter_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "chapter"

    def __init__(self, **kwargs):
        return super(ChapterDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ChapterDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ChapterDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ChapterDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ChapterDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ChapterDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ChapterDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ChapterDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ChapterDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ChapterDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ChapterDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("chapter_list")
