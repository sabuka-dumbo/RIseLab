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
    
class Project(models.Model):
    title = models.CharField(max_length=150)
    description_geo = models.TextField()
    short_description_geo = models.TextField()
    description_eng = models.TextField()
    short_description_eng = models.TextField()
    uploaded_at = models.DateField()
    image = models.ImageField(upload_to='projects_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
class Future_projects(models.Model):
    title = models.CharField(max_length=150)
    description_geo = models.TextField()
    short_description_geo = models.TextField()
    description_eng = models.TextField()
    short_description_eng = models.TextField()

    def __str__(self):
        return f"{self.title}"