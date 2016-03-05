# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TenderITApp', '0006_auto_20160228_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_templates',
            name='budget',
            field=models.IntegerField(),
        ),
    ]
