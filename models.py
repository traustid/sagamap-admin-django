# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chapters(models.Model):
    title = models.CharField(max_length=255)
    chapter = models.IntegerField()
    text = models.TextField()
    saga = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chapters'


class Placeattr(models.Model):
    type = models.CharField(max_length=10)
    place = models.IntegerField()
    attr1 = models.CharField(max_length=255)
    attr2 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'placeattr'


class Places(models.Model):
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    info = models.TextField()
    info2 = models.TextField()
    pkey = models.CharField(max_length=255)
    parish = models.CharField(max_length=255)
    county = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'places'


class Sagaplace(models.Model):
    place = models.IntegerField()
    saga = models.IntegerField()
    chapter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sagaplace'


class Sagas(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()
    defaultsaga = models.IntegerField()
    type = models.CharField(max_length=10)
    visible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sagas'


class Users(models.Model):
    uname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'