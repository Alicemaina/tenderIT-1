# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TenderITApp', '0005_auto_20160228_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_templates',
            name='budget',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
