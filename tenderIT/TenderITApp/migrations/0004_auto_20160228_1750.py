# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('TenderITApp', '0003_auto_20160226_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_templates',
            name='name',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(regex=b'^\\w{3}$', message=b'Length has to be 3', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='company_templates',
            name='nationalID',
            field=models.CharField(unique=True, max_length=64, validators=[django.core.validators.RegexValidator(regex=b'^\\w{3}$', message=b'Length has to be 3', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='company_templates',
            name='username',
            field=models.CharField(unique=True, max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\w{6}$', message=b'Length has to be 6', code=b'nomatch')]),
        ),
    ]
