from django.contrib import admin
from .models import Chapter, Placeattr, Place, Sagaplace, Saga
from django_baker.admin import ExtendedModelAdminMixin


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


class SagaChaptersInline(admin.TabularInline):
	model = Chapter


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
