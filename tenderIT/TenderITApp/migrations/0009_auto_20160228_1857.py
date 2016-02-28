# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('TenderITApp', '0008_auto_20160228_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='nationalID',
            field=models.CharField(unique=True, max_length=64, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='company',
            name='password',
            field=models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='company',
            name='username',
            field=models.CharField(unique=True, max_length=16, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
    ]
