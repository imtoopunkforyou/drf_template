# Generated by Django 4.0.5 on 2022-06-26 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('someapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.IntegerField(verbose_name='Длительность в секундах'),
        ),
        migrations.AlterField(
            model_name='track',
            name='order',
            field=models.PositiveSmallIntegerField(verbose_name='Номер композиции'),
        ),
    ]
