# Generated by Django 4.1.3 on 2023-04-12 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_upload'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Upload',
            new_name='File',
        ),
    ]
