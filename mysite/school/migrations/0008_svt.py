# Generated by Django 4.2 on 2023-11-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_alter_store_tecnumber_alter_store_technincs'),
    ]

    operations = [
        migrations.CreateModel(
            name='SVT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('acounting', models.CharField(max_length=100)),
                ('inv_number', models.CharField(max_length=50)),
                ('cmo', models.CharField(max_length=5000)),
                ('data_get', models.CharField(default='00.00.0000', max_length=50)),
                ('data_inp', models.CharField(default='00.00.0000', max_length=50)),
                ('quantity', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'СВТ',
                'verbose_name_plural': 'СВТ',
            },
        ),
    ]
