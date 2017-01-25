# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgreementAcceptance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='AgreementVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('agreement', models.ForeignKey(to='legal.Agreement')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='agreementacceptance',
            name='agreement_version',
            field=models.ForeignKey(to='legal.AgreementVersion'),
        ),
        migrations.AddField(
            model_name='agreementacceptance',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='agreementversion',
            unique_together=set([('agreement', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='agreementacceptance',
            unique_together=set([('user', 'agreement_version', 'date')]),
        ),
    ]
