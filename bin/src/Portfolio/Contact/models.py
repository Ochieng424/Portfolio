from django.db import models


# Create your models here.
class Contact(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    datestamp = models.DateTimeField(auto_now_add=True)
