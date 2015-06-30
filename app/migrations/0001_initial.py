# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution', models.CharField(max_length=128)),
                ('specialization', models.CharField(max_length=128)),
                ('graduated_at', models.DateField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('desc', models.CharField(max_length=1024, null=True)),
                ('duration', models.CharField(max_length=128, null=True)),
                ('role', models.CharField(max_length=128, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('level', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=16, null=True)),
                ('marital_status', models.CharField(max_length=16, null=True)),
                ('summary', models.CharField(max_length=2048, null=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('address', models.CharField(max_length=128, null=True)),
                ('phone', models.CharField(max_length=32, null=True)),
                ('skype', models.CharField(max_length=32, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
                ('score', models.FloatField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('resume', models.ForeignKey(to='app.Resume')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='language',
            name='resume',
            field=models.ForeignKey(to='app.Resume'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(to='app.Resume'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(to='app.Resume'),
            preserve_default=True,
        ),
    ]
