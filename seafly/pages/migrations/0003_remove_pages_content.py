# Generated by Django 3.0.4 on 2020-03-22 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200323_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pages',
            name='content',
        ),
    ]