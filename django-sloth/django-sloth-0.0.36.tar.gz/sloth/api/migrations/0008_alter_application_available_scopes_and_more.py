# Generated by Django 4.0.4 on 2022-05-28 10:56

from django.db import migrations
import sloth.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_scope_description_alter_task_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='available_scopes',
            field=sloth.db.models.ManyToManyField(blank=True, related_name='s1', to='api.scope'),
        ),
        migrations.AlterField(
            model_name='application',
            name='default_scopes',
            field=sloth.db.models.ManyToManyField(blank=True, related_name='s2', to='api.scope'),
        ),
    ]
