# Generated by Django 4.1.13 on 2023-11-17 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogModel',
            new_name='PostModel',
        ),
    ]
