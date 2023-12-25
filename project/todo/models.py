from django.db import models
from django.utils import timezone


class ToDo(models.Model):
     task = models.TextField()
     create_date = models.DateTimeField(default=timezone.now)

     def __str__(self):
          return self.task
	
     class Meta:
          ordering = ['create_date']
          verbose_name_plural = "Tasks"