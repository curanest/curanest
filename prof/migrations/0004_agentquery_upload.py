# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_agentquery_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentquery',
            name='upload',
            field=models.FileField(default='abc', upload_to=b'uploads/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
