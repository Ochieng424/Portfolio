from django.db import models


# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    live_project_link = models.URLField(max_length=100, blank=True)
    source_code_link = models.URLField(max_length=100)
    datestamp = models.DateTimeField(auto_now_add=True)
