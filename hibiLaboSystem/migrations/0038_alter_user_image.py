# Generated by Django 5.0.1 on 2024-02-29 08:50

import hibiLaboSystem.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hibiLaboSystem', '0037_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=hibiLaboSystem.models.unique_image_filename, verbose_name='アバター'),
        ),
    ]
