# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TenderITApp', '0009_auto_20160228_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_templates',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
