# Generated by Django 4.1.3 on 2023-04-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Adress',
        ),
        migrations.RemoveField(
            model_name='castomer',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='accounting',
            name='tecNumber',
            field=models.IntegerField(verbose_name='Техномер'),
        ),
        migrations.AlterField(
            model_name='accounting',
            name='technincs',
            field=models.CharField(max_length=50, verbose_name='Техника'),
        ),
        migrations.AlterField(
            model_name='accounting',
            name='users',
            field=models.CharField(max_length=30, verbose_name='Пользователь'),
        ),
        migrations.DeleteModel(
            name='Castomer',
        ),
    ]
