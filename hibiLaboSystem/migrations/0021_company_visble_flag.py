# Generated by Django 4.2.2 on 2024-02-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hibiLaboSystem', '0020_alter_bonknowevaluationperiod_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='visble_flag',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='HONNE社員名表示'),
        ),
    ]
