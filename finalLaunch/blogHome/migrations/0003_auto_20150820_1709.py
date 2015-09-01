# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogHome', '0002_auto_20150813_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestedpeople',
            name='phone_number',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
