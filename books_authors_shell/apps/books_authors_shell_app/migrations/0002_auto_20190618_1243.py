# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-18 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_shell_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='notes text field'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='Author', to='books_authors_shell_app.Book'),
        ),
    ]
