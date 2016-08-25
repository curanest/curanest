# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_auto_20160823_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentquery',
            name='photo',
            field=models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True),
        ),
    ]
