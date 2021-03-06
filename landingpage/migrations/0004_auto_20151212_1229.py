# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0003_sponsor_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='category',
            field=models.CharField(choices=[(b'Organizer', b'Organized by'), (b'Platinum', b'Co-presented to by'), (b'Gold', b'In Cooperation with'), (b'Silver', b'Also brought to you by'), (b'Bronze', b'Special thanks to'), (b'Media', b'Media Sponsors'), (b'Community', b'Community Partners')], max_length=10),
        ),
    ]
