# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('TenderITApp', '0004_auto_20160228_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
