from django.db import models


# Create your models here.
class MySkill(models.Model):
    title = models.CharField(max_length=50)
    rating = models.DecimalField(decimal_places=0, max_digits=3)
    datestamp = models.DateTimeField(auto_now_add=True, null=True)
