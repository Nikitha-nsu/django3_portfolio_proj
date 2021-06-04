from django.db import models
from django.utils import timezone

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now())
    description = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
