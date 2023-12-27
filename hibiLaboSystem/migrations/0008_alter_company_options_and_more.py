# Generated by Django 4.2.2 on 2023-11-30 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hibiLaboSystem', '0007_alter_mandaraprogress_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': '会社', 'verbose_name_plural': '会社'},
        ),
        migrations.AlterModelOptions(
            name='honneevaluationperiod',
            options={'verbose_name': 'HONNE 評価期間', 'verbose_name_plural': 'HONNE 評価期間'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'ユーザー', 'verbose_name_plural': 'ユーザー'},
        ),
        migrations.AddField(
            model_name='mandarabase',
            name='field_stop',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='mandarabase',
            name='flg_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='active_flag',
            field=models.BooleanField(blank=True, null=True, verbose_name='アクティブ'),
        ),
        migrations.AlterField(
            model_name='company',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='終了日'),
        ),
        migrations.AlterField(
            model_name='company',
            name='date_start',
            field=models.DateField(blank=True, null=True, verbose_name='開始日'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='会社名'),
        ),
        migrations.AlterField(
            model_name='company',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='companies', to='hibiLaboSystem.partner', verbose_name='相棒'),
        ),
        migrations.AlterField(
            model_name='honneevaluationperiod',
            name='evaluation_end',
            field=models.DateField(blank=True, null=True, verbose_name='評価終了時間'),
        ),
        migrations.AlterField(
            model_name='honneevaluationperiod',
            name='evaluation_name',
            field=models.CharField(max_length=255, verbose_name='評価名'),
        ),
        migrations.AlterField(
            model_name='honneevaluationperiod',
            name='evaluation_start',
            field=models.DateField(blank=True, null=True, verbose_name='評価開始時間'),
        ),
        migrations.AlterField(
            model_name='honneevaluationperiod',
            name='honne_questions',
            field=models.ManyToManyField(blank=True, related_name='honne_evaluation_periods', to='hibiLaboSystem.honnequestion', verbose_name='HONNE質問'),
        ),
    ]