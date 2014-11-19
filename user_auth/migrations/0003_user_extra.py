# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_auth', '0002_auto_20141119_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_number', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=30, blank=True)),
                ('city', models.CharField(max_length=30, blank=True)),
                ('county', models.CharField(max_length=30, blank=True)),
                ('commercial_district', models.CharField(max_length=30, blank=True)),
                ('identity_card_number', models.CharField(max_length=30, blank=True)),
                ('identity_card_image', models.ImageField(upload_to=b'identity_card', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
