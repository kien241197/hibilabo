# Generated by Django 5.0.1 on 2024-02-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hibiLaboSystem', '0025_watasheettyperesult_team_vision_10_years_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watasheettyperesult',
            name='team_action_10_years',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watasheettyperesult',
            name='team_action_1_year',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watasheettyperesult',
            name='team_action_5_years',
            field=models.TextField(blank=True, null=True),
        ),
    ]
