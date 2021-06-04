from django.db import models
from django.utils import timezone
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=timezone.now())


# Create your models here.
    def __str__(self):
        return self.title
