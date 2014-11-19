# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corporation_profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='corporation_profile',
            name='commercial_district',
        ),
        migrations.RemoveField(
            model_name='corporation_profile',
            name='county',
        ),
        migrations.RemoveField(
            model_name='corporation_profile',
            name='identity_card_image',
        ),
        migrations.RemoveField(
            model_name='corporation_profile',
            name='identity_card_number',
        ),
        migrations.RemoveField(
            model_name='corporation_profile',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='corporation_profile',
            name='province',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='commercial_district',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='county',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='identity_card_image',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='identity_card_number',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='employee_profile',
            name='province',
        ),
    ]
