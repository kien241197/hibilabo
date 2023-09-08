# Generated by Django 4.2.2 on 2023-09-08 07:34

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birth', models.DateField(blank=True, null=True)),
                ('role_id', models.IntegerField(blank=True, choices=[(99, '日々研'), (40, 'Partner'), (30, 'Company Admin'), (20, 'Company Super Visor'), (10, 'Company Staff')], null=True)),
                ('preferred_day', models.BooleanField(blank=True, null=True)),
                ('preferred_hour', models.IntegerField(blank=True, null=True)),
                ('preferred_day2', models.BooleanField(blank=True, null=True)),
                ('preferred_hour2', models.IntegerField(blank=True, null=True)),
                ('preferred_day3', models.BooleanField(blank=True, null=True)),
                ('preferred_hour3', models.IntegerField(blank=True, null=True)),
                ('preferred_day4', models.BooleanField(blank=True, null=True)),
                ('preferred_hour4', models.IntegerField(blank=True, null=True)),
                ('preferred_day5', models.BooleanField(blank=True, null=True)),
                ('preferred_hour5', models.IntegerField(blank=True, null=True)),
                ('preferred_day6', models.BooleanField(blank=True, null=True)),
                ('preferred_hour6', models.IntegerField(blank=True, null=True)),
                ('preferred_day7', models.BooleanField(blank=True, null=True)),
                ('preferred_hour7', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BonknowEvaluationPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_name', models.TextField()),
                ('evaluation_start', models.DateField(blank=True, null=True)),
                ('evaluation_end', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bonknow_evaluation_periods',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('active_flag', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='HonneEvaluationPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_name', models.TextField()),
                ('evaluation_start', models.DateField(blank=True, null=True)),
                ('evaluation_end', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_evaluation_periods', to='hibiLaboSystem.company')),
            ],
            options={
                'db_table': 'honne_evaluation_periods',
            },
        ),
        migrations.CreateModel(
            name='HonneQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('sort_no', models.IntegerField(blank=True, null=True)),
                ('acc1', models.BooleanField(default=False, verbose_name='1当てはまる')),
                ('acc2', models.BooleanField(default=False, verbose_name='2当てはまる')),
                ('acc3', models.BooleanField(default=False, verbose_name='3当てはまる')),
                ('acc4', models.BooleanField(default=False, verbose_name='4当てはまる')),
                ('acc5', models.BooleanField(default=False, verbose_name='5当てはまる')),
                ('acc6', models.BooleanField(default=False, verbose_name='6当てはまる')),
                ('acc7', models.BooleanField(default=False, verbose_name='7当てはまる')),
                ('acc8', models.BooleanField(default=False, verbose_name='8当てはまる')),
                ('group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True, verbose_name='カルテット分布')),
                ('apply_start_date', models.DateField(blank=True, null=True)),
                ('apply_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'honne_questions',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('time_start', models.DateTimeField(blank=True, null=True)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('active_flag', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'partners',
            },
        ),
        migrations.CreateModel(
            name='ResponsQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('sort_no', models.IntegerField(blank=True, null=True)),
                ('question_type', models.CharField(choices=[(1, 'Logic'), (2, 'Sense')], max_length=1, null=True)),
                ('apply_start_date', models.DateField(blank=True, null=True)),
                ('apply_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'respons_questions',
            },
        ),
        migrations.CreateModel(
            name='SelfcheckEvaluationPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_name', models.TextField()),
                ('evaluation_start', models.DateField(blank=True, null=True)),
                ('evaluation_end', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_evaluation_periods', to='hibiLaboSystem.company')),
            ],
            options={
                'db_table': 'selfcheck_evaluation_periods',
            },
        ),
        migrations.CreateModel(
            name='SelfcheckQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('sort_no', models.IntegerField(blank=True, null=True)),
                ('category_id', models.IntegerField(blank=True, choices=[(1, '決断力'), (2, '専門性'), (3, '自己管理'), (4, '広報力'), (5, '連携力'), (6, '人間関係'), (7, '患者対応'), (8, 'チームワーク力'), (9, '総合管理'), (10, '理念浸透'), (11, '自己啓発'), (12, '思考')], null=True)),
            ],
            options={
                'db_table': 'selfcheck_questions',
            },
        ),
        migrations.CreateModel(
            name='ThinkQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('sort_no', models.IntegerField(blank=True, null=True)),
                ('question_type', models.CharField(choices=[(1, 'Must'), (2, 'Want')], max_length=1, null=True)),
                ('apply_start_date', models.DateField(blank=True, null=True)),
                ('apply_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'think_questions',
            },
        ),
        migrations.CreateModel(
            name='ThinkResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('must', models.IntegerField(blank=True, default=0, null=True)),
                ('want', models.IntegerField(blank=True, default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='think_results', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='think_results', to='hibiLaboSystem.bonknowevaluationperiod')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='think_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'think_results',
            },
        ),
        migrations.CreateModel(
            name='ThinkAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(blank=True, null=True)),
                ('answer_date', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='think_answers', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='think_answers', to='hibiLaboSystem.bonknowevaluationperiod')),
                ('think_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='think_answers', to='hibiLaboSystem.thinkquestion')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='think_answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'think_answers',
            },
        ),
        migrations.CreateModel(
            name='SelfcheckTypeResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfcheck_circl', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_square', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_traiangle', models.IntegerField(blank=True, default=0, null=True)),
                ('flg_finished', models.BooleanField(default=False)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_type_results', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_type_results', to='hibiLaboSystem.selfcheckevaluationperiod')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_type_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'selfcheck_type_results',
            },
        ),
        migrations.CreateModel(
            name='SelfcheckIndexResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfcheck_index1', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index2', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index3', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index4', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index5', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index6', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index7', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index8', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index9', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index10', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index11', models.IntegerField(blank=True, default=0, null=True)),
                ('selfcheck_index12', models.IntegerField(blank=True, default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_index_results', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_index_results', to='hibiLaboSystem.selfcheckevaluationperiod')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_index_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'selfcheck_index_results',
            },
        ),
        migrations.AddField(
            model_name='selfcheckevaluationperiod',
            name='selfcheck_questions',
            field=models.ManyToManyField(blank=True, related_name='selfcheck_evaluation_periods', to='hibiLaboSystem.selfcheckquestion'),
        ),
        migrations.CreateModel(
            name='SelfcheckAnswerResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfcheck_answer', models.IntegerField(blank=True, null=True)),
                ('selfcheck_answer_date', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_results', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_answer_results', to='hibiLaboSystem.selfcheckevaluationperiod')),
                ('selfcheck_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selfcheck_results', to='hibiLaboSystem.selfcheckquestion')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selfcheck_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'selfcheck_answer_results',
            },
        ),
        migrations.CreateModel(
            name='ResponsResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logic', models.IntegerField(blank=True, default=0, null=True)),
                ('sense', models.IntegerField(blank=True, default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='respons_results', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='respons_results', to='hibiLaboSystem.bonknowevaluationperiod')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='respons_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'respons_results',
            },
        ),
        migrations.CreateModel(
            name='ResponsAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(blank=True, null=True)),
                ('answer_date', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='respons_answers', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='respons_answers', to='hibiLaboSystem.bonknowevaluationperiod')),
                ('respons_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respons_answers', to='hibiLaboSystem.responsquestion')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='respons_answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'respons_answers',
            },
        ),
        migrations.CreateModel(
            name='HonneTypeResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kartet_type_a', models.IntegerField(blank=True, null=True)),
                ('kartet_type_b', models.IntegerField(blank=True, null=True)),
                ('kartet_type_c', models.IntegerField(blank=True, null=True)),
                ('kartet_type_d', models.IntegerField(blank=True, null=True)),
                ('flg_finished', models.BooleanField(default=False)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_type_results', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_type_results', to='hibiLaboSystem.honneevaluationperiod')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_type_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'honne_type_results',
            },
        ),
        migrations.CreateModel(
            name='HonneIndexResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kartet_index1', models.IntegerField(blank=True, null=True)),
                ('kartet_index2', models.IntegerField(blank=True, null=True)),
                ('kartet_index3', models.IntegerField(blank=True, null=True)),
                ('kartet_index4', models.IntegerField(blank=True, null=True)),
                ('kartet_index5', models.IntegerField(blank=True, null=True)),
                ('kartet_index6', models.IntegerField(blank=True, null=True)),
                ('kartet_index7', models.IntegerField(blank=True, null=True)),
                ('kartet_index8', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_index_results', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_index_results', to='hibiLaboSystem.honneevaluationperiod')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_index_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'honne_index_results',
            },
        ),
        migrations.AddField(
            model_name='honneevaluationperiod',
            name='honne_questions',
            field=models.ManyToManyField(blank=True, related_name='honne_evaluation_periods', to='hibiLaboSystem.honnequestion'),
        ),
        migrations.CreateModel(
            name='HonneAnswerResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField(default=False)),
                ('answer_date', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_results', to='hibiLaboSystem.company')),
                ('evaluation_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_answer_results', to='hibiLaboSystem.honneevaluationperiod')),
                ('honne_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='honne_results', to='hibiLaboSystem.honnequestion')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='honne_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'honne_answer_results',
            },
        ),
        migrations.CreateModel(
            name='Hierarchy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boss', to=settings.AUTH_USER_MODEL)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hierarchies',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='companies', to='hibiLaboSystem.partner'),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='branches', to='hibiLaboSystem.company')),
            ],
            options={
                'db_table': 'branches',
            },
        ),
        migrations.AddField(
            model_name='bonknowevaluationperiod',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bonknow_evaluation_periods', to='hibiLaboSystem.company'),
        ),
        migrations.AddField(
            model_name='bonknowevaluationperiod',
            name='respons_questions',
            field=models.ManyToManyField(blank=True, related_name='bonknow_evaluation_periods', to='hibiLaboSystem.responsquestion'),
        ),
        migrations.AddField(
            model_name='bonknowevaluationperiod',
            name='think_questions',
            field=models.ManyToManyField(blank=True, related_name='bonknow_evaluation_periods', to='hibiLaboSystem.thinkquestion'),
        ),
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='hibiLaboSystem.branch'),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='hibiLaboSystem.company'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='hierarchy',
            field=models.ManyToManyField(blank=True, through='hibiLaboSystem.Hierarchy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
