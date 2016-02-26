# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TenderITApp', '0002_auto_20160226_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='webiste',
            new_name='website',
        ),
    ]
