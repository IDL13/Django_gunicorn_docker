# Generated by Django 4.0.5 on 2022-07-06 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_user_alter_adress_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
