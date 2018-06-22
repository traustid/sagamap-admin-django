from django.db import models

class SagaChapterField(models.Field):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def deconstruct(self):
		name, path, args, kwargs = super().deconstruct()
		return name, path, args, kwargs