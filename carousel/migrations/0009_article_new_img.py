# Generated by Django 2.0.7 on 2019-07-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0008_auto_20190716_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='new_img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]