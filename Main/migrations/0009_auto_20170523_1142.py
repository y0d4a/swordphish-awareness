# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-23 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20170330_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='fake_ransom',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='campaign_fake_ransom', to='Main.Template'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_type',
            field=models.CharField(choices=[(b'1', 'Simple'), (b'2', 'With Attachment'), (b'3', 'Fake Form'), (b'4', 'Fake Ransomware')], default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='template',
            name='template_type',
            field=models.CharField(choices=[(b'#1', 'Mail with link'), (b'1', 'Mail with link template'), (b'#2', 'Mail with attachment'), (b'2', 'Mail with attachment template'), (b'3', 'Attachment template'), (b'#3', 'Action after click'), (b'4', 'Redirection'), (b'5', 'Awareness template'), (b'6', 'Fake form template'), (b'7', 'Fake ransomware template')], default=1, max_length=1),
        ),
    ]
