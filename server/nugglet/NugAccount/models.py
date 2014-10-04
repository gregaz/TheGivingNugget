from django.db import models

# Create your models here.
class NugAccount(models.Model):
	name = models.TextField()
	balance = models.IntegerField()
	linkedAccount = models.TextField()

	def __str__(self):
		return self.name

	class Admin:
		list_display = ('name', 'balance')
		search_fields = ('name',)