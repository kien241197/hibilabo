# Generated by Django 5.0.1 on 2024-02-29 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hibiLaboSystem', '0032_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/assets/images'),
        ),
    ]
