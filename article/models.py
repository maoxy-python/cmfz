from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class Carousel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.ImageField(upload_to='img')
    status = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    # content = RichTextUploadingField(null=True, blank=True)

    class Meta:
        db_table = 'carousel'


class Caption(models.Model):

    title = models.CharField(max_length=128, blank=True, null=True)
    size = models.CharField(max_length=10)
    time = models.CharField(max_length=28)
    audio = models.FileField(upload_to="upload/audio")

    class Meta:
        db_table = 't_caption'

