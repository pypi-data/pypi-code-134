# Generated by Django 2.2 on 2020-01-17 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyn_struct', '0005_auto_20160913_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicstructurefield',
            name='name',
            field=models.CharField(blank=True, max_length=512, verbose_name='Название'),
        ),
    ]
