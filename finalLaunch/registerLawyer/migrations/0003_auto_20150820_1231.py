# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerLawyer', '0002_auto_20150820_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyerregisterdetail',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
