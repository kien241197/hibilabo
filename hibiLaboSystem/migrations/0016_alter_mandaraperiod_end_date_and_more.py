# Generated by Django 5.0 on 2023-12-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hibiLaboSystem', '0015_alter_mandaraperiod_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mandaraperiod',
            name='end_date',
            field=models.DateField(verbose_name='評価終了時間'),
        ),
        migrations.AlterField(
            model_name='mandaraperiod',
            name='start_date',
            field=models.DateField(verbose_name='評価開始時間'),
        ),
    ]
