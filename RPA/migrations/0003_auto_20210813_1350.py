# Generated by Django 3.2.6 on 2021-08-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPA', '0002_alter_cliente_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo_contacto',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Correo para contactar'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateField(blank=True, verbose_name='Fecha de realizacion de la cotizacion'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='lugar_de_mantenimiento',
            field=models.CharField(blank=True, max_length=120, verbose_name='Lugar en que se realizara el mantenimiento'),
        ),
    ]