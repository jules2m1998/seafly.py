# Generated by Django 3.0.4 on 2020-03-23 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_pages_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='content',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]