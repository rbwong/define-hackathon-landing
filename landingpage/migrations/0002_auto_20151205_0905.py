# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='picture',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='picture',
            field=models.ImageField(upload_to=b''),
        ),
    ]
