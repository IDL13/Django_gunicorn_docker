# Generated by Django 4.0.5 on 2022-07-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_accounting_options_alter_adress_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounting',
            name='create',
            field=models.DateField(auto_now=True),
        ),
    ]
