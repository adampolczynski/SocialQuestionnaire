from django.db import models
from django.contrib import admin

# Create your models here.

class Questions(models.Model):
	question = models.CharField(max_length=30)
	wages_1 = models.TextField()
	wages_2 = models.TextField()
	wages_3 = models.TextField()
	wages_4 = models.TextField()
	wages_5 = models.TextField()


	class Meta:
		db_table = 'questions'
admin.site.register(Questions)