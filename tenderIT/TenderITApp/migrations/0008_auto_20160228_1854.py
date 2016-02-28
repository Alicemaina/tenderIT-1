# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('TenderITApp', '0007_auto_20160228_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
