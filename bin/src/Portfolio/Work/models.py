from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import requests


# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    image_url = models.CharField(max_length=255, null=True, blank=True)
    live_project_link = models.URLField(max_length=100, blank=True)
    source_code_link = models.URLField(max_length=100)
    datestamp = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Work)
def work_post_save(**kwargs):
    print(kwargs)
    instance = kwargs.get("instance")
    upload_image(instance.id, instance.image.path)


def upload_image(id, file_path):
    files = {
        'upload': open(file_path, 'rb')
    }

    response = requests.post(url="https://projects.cognition.co.ke/file-upload/index.php", files=files)
    if response.status_code == 201:
        print("RESPONSE: {0}".format(response.json()))
        response_data = response.json()
        Work.objects.filter(id=id).update(image_url=response_data['file'])
    else:
        print("ERROR: {0}".format(response.json()))