# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradingsystem', '0003_book_conservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradingsystem.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradingsystem.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailAdvertiser', models.CharField(max_length=200)),
                ('emailOfferor', models.CharField(max_length=200)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradingsystem.Ad')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradingsystem.Offer')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='cidade', max_length=200),
            preserve_default=False,
        ),
    ]
