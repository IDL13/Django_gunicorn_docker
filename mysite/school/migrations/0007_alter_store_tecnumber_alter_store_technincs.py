# Generated by Django 4.1.3 on 2023-04-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_store_tecnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='tecNumber',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='store',
            name='technincs',
            field=models.CharField(max_length=500),
        ),
    ]
