# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default=b'male', max_length=10, choices=[(b'male', b'Male'), (b'female', b'Female')])),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True)),
                ('mobilenumber', models.CharField(max_length=15, null=True)),
                ('address', models.TextField(null=True)),
                ('photo', models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AgentQuery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=30)),
                ('mobilenumber', models.CharField(max_length=15)),
                ('agent', models.ForeignKey(to='prof.AgentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=30)),
                ('mobilenumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True)),
                ('mobilenumber', models.CharField(default=None, max_length=15)),
                ('address', models.TextField(null=True)),
                ('photo', models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalQuery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hospital', models.ForeignKey(to='prof.HospitalProfile')),
            ],
        ),
        migrations.CreateModel(
            name='NewAgentQuery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=30)),
                ('mobilenumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usertype', models.CharField(max_length=20, null=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default=b'male', max_length=10, choices=[(b'male', b'Male'), (b'female', b'Female')])),
                ('allergies', models.CharField(max_length=50, null=True)),
                ('medicalhistory', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True)),
                ('mobilenumber', models.CharField(max_length=15, null=True)),
                ('address', models.TextField(null=True)),
                ('photo', models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('agent', models.ForeignKey(related_name='agent_queries', to='prof.AgentProfile')),
                ('hospital', models.ManyToManyField(to='prof.HospitalProfile', through='prof.HospitalQuery')),
                ('user', models.ForeignKey(related_name='queries', to='prof.PatientProfile')),
            ],
        ),
        migrations.CreateModel(
            name='QueryImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True)),
                ('query', models.ForeignKey(related_name='query_images', to='prof.Query')),
            ],
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='query',
            field=models.OneToOneField(to='prof.Query'),
        ),
        migrations.AddField(
            model_name='hospitalquery',
            name='query',
            field=models.ForeignKey(to='prof.Query'),
        ),
        migrations.AddField(
            model_name='hospitalimages',
            name='hospital',
            field=models.ForeignKey(related_name='hospital_images', to='prof.HospitalProfile'),
        ),
    ]
