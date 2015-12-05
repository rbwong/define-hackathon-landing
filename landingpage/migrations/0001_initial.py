# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=50)),
                ('picture', models.ImageField(height_field=200, width_field=200, upload_to=b'')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('picture', models.ImageField(height_field=200, width_field=200, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('m1_full_name', models.CharField(max_length=50)),
                ('m1_school', models.CharField(max_length=50)),
                ('m1_course', models.CharField(max_length=50)),
                ('m1_contact_num', models.CharField(max_length=50)),
                ('m1_email', models.EmailField(max_length=50)),
                ('m2_full_name', models.CharField(max_length=50)),
                ('m2_school', models.CharField(max_length=50)),
                ('m2_course', models.CharField(max_length=50)),
                ('m2_contact_num', models.CharField(max_length=50)),
                ('m2_email', models.EmailField(max_length=50)),
                ('m3_full_name', models.CharField(max_length=50)),
                ('m3_school', models.CharField(max_length=50)),
                ('m3_course', models.CharField(max_length=50)),
                ('m3_contact_num', models.CharField(max_length=50)),
                ('m3_email', models.EmailField(max_length=50)),
                ('m4_full_name', models.CharField(max_length=50, null=True, blank=True)),
                ('m4_school', models.CharField(max_length=50, null=True, blank=True)),
                ('m4_course', models.CharField(max_length=50, null=True, blank=True)),
                ('m4_contact_num', models.CharField(max_length=50, null=True, blank=True)),
                ('m4_email', models.EmailField(max_length=50, null=True, blank=True)),
                ('m5_full_name', models.CharField(max_length=50, null=True, blank=True)),
                ('m5_school', models.CharField(max_length=50, null=True, blank=True)),
                ('m5_course', models.CharField(max_length=50, null=True, blank=True)),
                ('m5_contact_num', models.CharField(max_length=50, null=True, blank=True)),
                ('m5_email', models.EmailField(max_length=50, null=True, blank=True)),
            ],
        ),
    ]
