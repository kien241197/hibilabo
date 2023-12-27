# Generated by Django 4.2.2 on 2023-12-12 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hibiLaboSystem', '0013_alter_bonknowevaluationperiod_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MandaraPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='mandarabase',
            name='unique_mandara',
        ),
        migrations.RemoveField(
            model_name='mandarabase',
            name='end_YYYYMM',
        ),
        migrations.RemoveField(
            model_name='mandarabase',
            name='start_YYYYMM',
        ),
        migrations.AddField(
            model_name='mandaraperiod',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mandara_periods', to='hibiLaboSystem.company'),
        ),
        migrations.AddField(
            model_name='mandarabase',
            name='mandara_period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mandara_base', to='hibiLaboSystem.mandaraperiod'),
        ),
    ]