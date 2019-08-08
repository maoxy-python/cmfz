# Generated by Django 2.0.7 on 2019-07-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.ImageField(upload_to='img')),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'carousel',
            },
        ),
    ]
