# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-29 15:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32, unique=True)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('port', models.IntegerField(default=22)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_type', models.SmallIntegerField(choices=[(1, 'ssh_password'), (2, 'ssh_key')])),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostUserBind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.Host')),
                ('host_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.HostUser')),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='hostuser',
            unique_together=set([('username', 'password')]),
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='host_user_binds',
            field=models.ManyToManyField(to='audit.HostUserBind'),
        ),
        migrations.AddField(
            model_name='host',
            name='host_user',
            field=models.ManyToManyField(to='audit.HostUser'),
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.IDC'),
        ),
        migrations.AddField(
            model_name='account',
            name='host',
            field=models.ManyToManyField(to='audit.HostUserBind'),
        ),
        migrations.AddField(
            model_name='account',
            name='host_group',
            field=models.ManyToManyField(to='audit.HostGroup'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='hostuserbind',
            unique_together=set([('host', 'host_user')]),
        ),
    ]
