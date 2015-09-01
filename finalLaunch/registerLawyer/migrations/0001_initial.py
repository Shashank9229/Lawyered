# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LawyerRegisterDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100, blank=True)),
                ('city_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200, blank=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('state_bar_no', models.CharField(max_length=50, blank=True)),
                ('bar_council_no', models.CharField(max_length=50, blank=True)),
                ('terms_conditions', models.BooleanField(default=False)),
                ('register_time', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
        ),
    ]
