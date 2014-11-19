# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='corporation_profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_number', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=30, blank=True)),
                ('city', models.CharField(max_length=30, blank=True)),
                ('county', models.CharField(max_length=30, blank=True)),
                ('commercial_district', models.CharField(max_length=30, blank=True)),
                ('identity_card_number', models.CharField(max_length=30, blank=True)),
                ('identity_card_image', models.ImageField(upload_to=b'identity_card', blank=True)),
                ('corporation_name', models.CharField(max_length=30, blank=True)),
                ('business_license', models.CharField(max_length=50, blank=True)),
                ('business_license_image', models.ImageField(upload_to=b'business_license', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='employee_profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_number', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=30, blank=True)),
                ('city', models.CharField(max_length=30, blank=True)),
                ('county', models.CharField(max_length=30, blank=True)),
                ('commercial_district', models.CharField(max_length=30, blank=True)),
                ('identity_card_number', models.CharField(max_length=30, blank=True)),
                ('identity_card_image', models.ImageField(upload_to=b'identity_card', blank=True)),
                ('real_name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=1, choices=[(b'M', b'\xe7\x94\xb7\xe6\x80\xa7'), (b'F', b'\xe5\xa5\xb3\xe6\x80\xa7')])),
                ('birthday', models.DateField()),
                ('workon', models.CharField(max_length=b'30', choices=[(b'student', b'\xe5\xad\xa6\xe7\x94\x9f'), (b'working', b'\xe5\x9c\xa8\xe8\x81\x8c'), (b'work at home', b'\xe8\x87\xaa\xe7\x94\xb1\xe8\x81\x8c\xe4\xb8\x9a\xe8\x80\x85'), (b'other', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
