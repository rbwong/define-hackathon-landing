# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_auto_20151205_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='category',
            field=models.CharField(choices=[(b'Platinum', b'Co-presented to by'), (b'Gold', b'In Cooperation with'), (b'Silver', b'Also brought to you by'), (b'Bronze', b'Special thanks to'), (b'Media', b'Media Sponsors')], default='Platinum', max_length=10),
            preserve_default=False,
        ),
    ]