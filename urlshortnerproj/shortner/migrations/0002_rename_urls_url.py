# Generated by Django 4.2.1 on 2023-05-27 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Urls',
            new_name='Url',
        ),
    ]