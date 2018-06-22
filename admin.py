from django.contrib import admin
from .models import Chapter, Placeattr, Place, Sagaplace, Saga
from django_baker.admin import ExtendedModelAdminMixin
from django.utils.safestring import mark_safe
from string import Template


class PlaceattrAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class SagaPlacesInline(admin.TabularInline):
	model = Sagaplace
#	raw_id_fields = ['person']
#	model._meta.verbose_name_plural = "Relaterade personer"


class PlaceAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	list_display = ['id', 'name', 'type', 'county']
	extra_list_display = []
	extra_list_filter = ['type', 'county']
	extra_search_fields = []
	list_editable = ['name', 'type', 'county']
	raw_id_fields = []
	inlines = [SagaPlacesInline]
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	fields = [('name', 'type'), ('lat', 'lng'), 'map_tag', 'info', 'info2', 'pkey', ('parish', 'county')]
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = ['map_tag']


class ChapterAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	list_display = ['id', 'title', 'chapter', 'saga']
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class SagaChaptersInline(admin.TabularInline):
	def chapter_html_tag(self, obj):
		values = {
			'html': str(obj.text),
			'obj_id': str(obj.id)
		}
		html_template = """
			<div class="chapter-html-content chapter-html-content-${obj_id}">${html}</div>
		"""

		template = Template(html_template)

		chapter_html = template.substitute(values)

		return mark_safe(chapter_html);

	chapter_html_tag.allow_tags = True

	model = Chapter
	fields = ['chapter', 'title', ('text', 'chapter_html_tag')]
	readonly_fields = ['chapter_html_tag']

	class Media:
		js = ['sagamap/selection.js', 'sagamap/saga-chapters.js']
		css = {
			'screen': ['sagamap/saga-chapters.css']
		}


class SagaAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	list_display = ['id', 'title', 'type', 'visible']
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = ['title', 'type', 'visible']
	raw_id_fields = []
	inlines = [SagaChaptersInline]
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class SagaplaceAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	list_display = ['id', 'place', 'chapter']
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


admin.site.register(Chapter, ChapterAdmin)
#admin.site.register(Placeattr, PlaceattrAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Sagaplace, SagaplaceAdmin)
admin.site.register(Saga, SagaAdmin)
