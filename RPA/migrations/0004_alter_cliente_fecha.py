# Generated by Django 3.2.6 on 2021-08-13 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPA', '0003_auto_20210813_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateField(auto_now=True, verbose_name='Fecha de realizacion de la cotizacion'),
        ),
    ]