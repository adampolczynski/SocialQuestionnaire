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

	# def as_dict(self):
	# 	return {
	# 	"question": self.id,
	# 	"wages_1": self.wages_1,
	# 	"wages_2": self.wages_2,
	# 	"wages_3": self.wages_3,
	# 	"wages_4": self.wages_4,
	# 	"wages_5": self.wages_5
 #            # other stuff
 #            }
	class Meta:
		db_table = 'questions'
admin.site.register(Questions)