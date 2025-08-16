from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150, default='')
    article = models.CharField(max_length=1000, default='')
    short_description = models.CharField(max_length=100, default='')
    created_at = models.DateField()
    updated_at = models.DateField()
    written_by = models.CharField(max_length=150, default='')

    def __str__(self):
        return f"{ self.title }"