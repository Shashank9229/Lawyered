# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerLawyer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyerregisterdetail',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, default='Male'),
        ),
    ]
