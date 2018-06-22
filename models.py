# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.safestring import mark_safe
from string import Template
from tinymce.models import HTMLField
#from ckeditor.fields import RichTextField

from .fields import SagaChapterField


class Place(models.Model):
	lat = models.FloatField(blank=True, null=True)
	lng = models.FloatField(blank=True, null=True)
	name = models.CharField(max_length=255)
	type = models.CharField(max_length=255)
	info = models.TextField()
	info2 = models.TextField()
	pkey = models.CharField(max_length=255)
	parish = models.CharField(max_length=255)
	county = models.CharField(max_length=255)

	def map_tag(self):
		values = {
			'lat': str(self.lat),
			'lng': str(self.lng)
		}
		map_template = """
			<link rel="stylesheet" href="https://unpkg.com/leaflet@1.2.0/dist/leaflet.css" />
			<script src="https://unpkg.com/leaflet@1.2.0/dist/leaflet.js"></script>
			<div id="place_map" style="width: 100%; height: 400px;"></div>
			<script type="text/javascript">
				var map = L.map("place_map").setView([${lat}, ${lng}], 8); // Skapar en karta
				L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {attribution: "&copy; <a href='http://osm.org/copyright'>OpenStreetMap</a> contributors"}).addTo(map);
				var marker = L.marker([${lat}, ${lng}]);
				marker.addTo(map);

				map.on('click', function(e) { // Map click handler
					marker.setLatLng(e.latlng); // Uppdaterar punkten på kartan

					django.jQuery('#id_lat').val(e.latlng.lat.toFixed(6)); // Skriver e.latlng.lat från punkter var man klickade på kartan till "lat" fältet
					django.jQuery('#id_lng').val(e.latlng.lng.toFixed(6)); // Skriver e.latlng.lng från punkter var man klickade på kartan till "lng" fältet
				});
			</script>
		"""

		template = Template(map_template)

		map_html = template.substitute(values)

		return mark_safe(map_html);

	map_tag.short_description = 'Map'
	map_tag.allow_tags = True

	def __str__(self):
		return self.name+' ('+self.type+') '

	class Meta:
		managed = False
		db_table = 'places'


class Placeattr(models.Model):
	type = models.CharField(max_length=10)
	place = models.ForeignKey(Place, on_delete=models.DO_NOTHING)
	attr1 = models.CharField(max_length=255)
	attr2 = models.CharField(max_length=255)

	class Meta:
		managed = False
		db_table = 'placeattr'


class Saga(models.Model):
	title = models.CharField(max_length=255)
	info = models.TextField(blank=True)
	defaultsaga = models.BooleanField()
	type = models.CharField(max_length=10)
	visible = models.BooleanField()

	def __str__(self):
		return self.title

	class Meta:
		managed = False
		db_table = 'sagas'


class Chapter(models.Model):
	title = models.CharField(max_length=255)
	chapter = models.IntegerField()
	text = models.TextField()
	saga = models.ForeignKey(Saga, on_delete=models.DO_NOTHING, db_column='saga')

	def chapter_html_tag(self):
		values = {
			'html': str(self.text)
		}
		html_template = """
			<div>${html}</div>
		"""

		template = Template(html_template)

		chapter_html = template.substitute(values)

		return mark_safe(chapter_html);

	chapter_html_tag.short_description = 'Chapter text'
	chapter_html_tag.allow_tags = True

	def __str__(self):
		return self.title+' ('+self.saga.title+')'

	class Meta:
		managed = False
		db_table = 'chapters'


class Sagaplace(models.Model):
	place = models.ForeignKey(Place, on_delete=models.DO_NOTHING, db_column='place')
#	saga = models.ForeignKey(Saga, on_delete=models.DO_NOTHING, db_column='saga')
	chapter = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING, db_column='chapter')

	class Meta:
		managed = False
		db_table = 'sagaplace'
