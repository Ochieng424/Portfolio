from django.db import models


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='', null=True)
    description = models.TextField()
    resume = models.FileField(upload_to='', blank=True, null=True)
    featured = models.BooleanField(default=False)
    datestamp = models.DateTimeField(auto_now_add=True)
