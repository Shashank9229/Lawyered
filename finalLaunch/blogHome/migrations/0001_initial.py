# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('article_title', models.CharField(unique=True, max_length=200, verbose_name='Enter the title of your article')),
                ('aritcle_slug', models.SlugField(unique=True, max_length=100)),
                ('article_body', models.TextField(verbose_name='Enter the body of article')),
                ('cover_image', models.ImageField(upload_to='')),
                ('article_author', models.CharField(max_length=100, verbose_name='Enter author name')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterestedPeople',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('person_email', models.EmailField(max_length=254)),
                ('person_city', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField(unique=True)),
            ],
        ),
    ]
