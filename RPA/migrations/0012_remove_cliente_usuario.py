# Generated by Django 3.2.5 on 2021-08-27 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RPA', '0011_merge_0008_auto_20210818_1201_0010_auto_20210826_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
    ]
