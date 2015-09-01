# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogHome', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='aritcle_slug',
            new_name='article_slug',
        ),
        migrations.AlterField(
            model_name='article',
            name='cover_image',
            field=models.ImageField(upload_to='blogHone/articleImages'),
        ),
    ]
