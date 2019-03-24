from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import requests


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='', null=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    resume = models.FileField(upload_to='', blank=True, null=True)
    featured = models.BooleanField(default=False)
    datestamp = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=About)
def about_post_save(**kwargs):
    print(kwargs)
    instance = kwargs.get("instance")
    upload_file(instance.id, instance.image.path)


def upload_file(id, file_path):
    files = {
        'upload': open(file_path, 'rb')
    }

    response = requests.post(url="https://projects.cognition.co.ke/file-upload/index.php", files=files)
    if response.status_code == 201:
        print("RESPONSE: {0}".format(response.json()))
        response_data = response.json()
        About.objects.filter(id=id).update(image_url=response_data['file'])
    else:
        print("ERROR: {0}".format(response.json()))
