# Generated by Django 4.1.1 on 2022-10-06 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0004_stage_visited'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='next_stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev', to='rpg.stage'),
        ),
        migrations.AddField(
            model_name='stage',
            name='previous_stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='rpg.stage'),
        ),
    ]
