# Generated by Django 3.2.6 on 2021-08-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPA', '0008_auto_20210824_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimiento',
            name='costomantenimientoadicional',
            field=models.FloatField(blank=True, null=True, verbose_name='horas por actividad de mtto adicional =Importe de cantidad x Tiempo de ejecucion '),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='costomantenimientoregular',
            field=models.FloatField(null=True, verbose_name='horas por actividad de mtto regular =Importe de cantidad x Tiempo de ejecucion'),
        ),
    ]
