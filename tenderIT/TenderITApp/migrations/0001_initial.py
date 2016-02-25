# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nationalID', models.CharField(unique=True, max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('postcode', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.BigIntegerField()),
                ('webiste', models.URLField()),
                ('username', models.CharField(unique=True, max_length=16)),
                ('password', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^\\w{6}$', message=b'Length has to be 6', code=b'nomatch')])),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('budget', models.IntegerField()),
                ('currency', models.CharField(default=b'USD', max_length=3, choices=[(b'USD', b'US Dollar'), (b'EUR', b'Euro'), (b'GBP', b'British Pound')])),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('documents', models.FileField(upload_to=b'uploads/')),
                ('slug', models.SlugField()),
                ('company', models.ForeignKey(to='TenderITApp.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('applicant', models.ForeignKey(to='TenderITApp.Company')),
                ('project', models.ForeignKey(to='TenderITApp.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField()),
                ('provider', models.ForeignKey(related_name=b'rating_provider', to='TenderITApp.Company')),
                ('receiver', models.ForeignKey(related_name=b'rating_receiver', to='TenderITApp.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
