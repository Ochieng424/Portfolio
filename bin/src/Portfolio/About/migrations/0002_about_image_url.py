# Generated by Django 2.1.7 on 2019-03-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
