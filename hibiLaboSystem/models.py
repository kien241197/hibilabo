from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum 
from django.core.exceptions import ValidationError

# Create your models here.
class Partner(models.Model):
	name = models.CharField(blank=True, null=True, max_length=255)
	time_start = models.DateTimeField(blank=True, null=True)
	time_end = models.DateTimeField(blank=True, null=True)
	active_flag = models.BooleanField(blank=True, null=True)

	class Meta:
		db_table = "partners"

	def __str__(self):
		return f"{self.name}"

class Company(models.Model):
	name = models.CharField(blank=True, null=True, max_length=255, verbose_name="会社名")
	date_start = models.DateField(blank=True, null=True, verbose_name='開始日')
	date_end = models.DateField(blank=True, null=True, verbose_name='終了日')
	active_flag = models.BooleanField(blank=True, null=True, verbose_name='アクティブ')
	partner = models.ForeignKey(
	    Partner,
	    on_delete=models.DO_NOTHING,
	    related_name='companies',
	    blank=True,
	    null=True,
	    verbose_name='相棒'
	)
	created_by = models.IntegerField(blank=True, null=True, editable=False)

	class Meta:
			db_table = "companies"
			verbose_name = '会社'
			verbose_name_plural = '会社'

	def __str__(self):
		return f"{self.name}"

class Branch(models.Model):
	name = models.CharField(blank=True, null=True, max_length=255)
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='branches',
	    blank=True,
	    null=True
	)

	class Meta:
		db_table = "branches"

	def __str__(self):
		return f"{self.name}"


class User(AbstractUser):
	class Roles(Enum):
		日々研 = 99
		Partner = 40
		CompanyAdmin = 30
		CompanySuperVisor = 20
		CompanyStaff = 10

	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='users',
	    blank=True,
	    null=True,
	    verbose_name='会社'
	)
	branch = models.ForeignKey(
	    Branch,
	    on_delete=models.DO_NOTHING,
	    related_name='users',
	    blank=True,
	    null=True,
	    verbose_name='支店'
	)
	birth = models.DateField(blank=True, null=True, verbose_name='誕生日')
	role_id = models.IntegerField(
		blank=True,
		null=True,
		choices=[
			(99, '日々研'),
			(40, 'Partner'),
			(30, 'Company Admin'),
			(20, 'Company Super Visor'),
			(10, 'Company Staff'),
		],
		verbose_name='役割'
    )
	preferred_day = models.BooleanField(blank=True, null=True)
	preferred_hour = models.IntegerField(blank=True, null=True)
	preferred_day2 = models.BooleanField(blank=True, null=True)
	preferred_hour2 = models.IntegerField(blank=True, null=True)
	preferred_day3 = models.BooleanField(blank=True, null=True)
	preferred_hour3 = models.IntegerField(blank=True, null=True)
	preferred_day4 = models.BooleanField(blank=True, null=True)
	preferred_hour4 = models.IntegerField(blank=True, null=True)
	preferred_day5 = models.BooleanField(blank=True, null=True)
	preferred_hour5 = models.IntegerField(blank=True, null=True)
	preferred_day6 = models.BooleanField(blank=True, null=True)
	preferred_hour6 = models.IntegerField(blank=True, null=True)
	preferred_day7 = models.BooleanField(blank=True, null=True)
	preferred_hour7 = models.IntegerField(blank=True, null=True)
	hierarchy = models.ManyToManyField('self', through='Hierarchy', symmetrical=False, blank=True)
	created_by = models.IntegerField(blank=True, null=True, editable=False)

	class Meta:
		db_table = 'users'
		verbose_name = 'ユーザー'
		verbose_name_plural = 'ユーザー'

	def full_name(self):
		return self.last_name + self.first_name

	def __str__(self):
		return f"{self.last_name + self.first_name}"

class Hierarchy(models.Model):
	boss = models.ForeignKey(
		User, 
		on_delete=models.CASCADE, 
		related_name='boss'
	)
	staff = models.ForeignKey(
    	User,
    	on_delete=models.CASCADE,
    	related_name='staff'
    )

	class Meta:
		db_table = 'hierarchies'

# HONNE
class HonneQuestion(models.Model):
	class Meta:
		verbose_name = 'HONNE質問'

	question = models.TextField()
	sort_no = models.IntegerField(blank=True, null=True)
	acc1 = models.BooleanField(default=False, verbose_name="1当てはまる")
	acc2 = models.BooleanField(default=False, verbose_name="2当てはまる")
	acc3 = models.BooleanField(default=False, verbose_name="3当てはまる")
	acc4 = models.BooleanField(default=False, verbose_name="4当てはまる")
	acc5 = models.BooleanField(default=False, verbose_name="5当てはまる")
	acc6 = models.BooleanField(default=False, verbose_name="6当てはまる")
	acc7 = models.BooleanField(default=False, verbose_name="7当てはまる")
	acc8 = models.BooleanField(default=False, verbose_name="8当てはまる")
	group = models.CharField(
		verbose_name="カルテット分布",
		max_length=1,
		null=True,
		choices=[
			('A', 'A'),
			('B', 'B'),
			('C', 'C'),
			('D', 'D'),
		]
	)
	apply_start_date = models.DateField(blank=True, null=True)
	apply_end_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'honne_questions'

	def __str__(self):
		return str(self.question)

class HonneEvaluationPeriod(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_evaluation_periods',
	    blank=True,
	    null=True
	)
	evaluation_name = models.CharField(max_length=255, verbose_name='評価名')
	evaluation_start = models.DateField(blank=True, null=True, verbose_name='評価開始時間')
	evaluation_end = models.DateField(blank=True, null=True, verbose_name='評価終了時間')
	honne_questions = models.ManyToManyField(
		HonneQuestion,
	    related_name='honne_evaluation_periods',
	    blank=True,
	    verbose_name = 'HONNE質問'
	)

	class Meta:
		db_table = 'honne_evaluation_periods'
		verbose_name = 'HONNE 評価期間'
		verbose_name_plural = 'HONNE 評価期間'

	def __str__(self):
		return f"{self.evaluation_name}"

class HonneAnswerResult(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_results',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_results',
	    blank=True,
	    null=True
	)
	honne_question = models.ForeignKey(
	    HonneQuestion,
	    on_delete=models.CASCADE,
	    related_name='honne_results'
	)
	evaluation_period = models.ForeignKey(
	    HonneEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_answer_results',
	    blank=True,
	    null=True
	)
	answer = models.BooleanField(default=False)
	answer_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'honne_answer_results'

class HonneIndexResult(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_index_results',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_index_results',
	    blank=True,
	    null=True
	)
	evaluation_period = models.ForeignKey(
	    HonneEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_index_results',
	    blank=True,
	    null=True
	)
	kartet_index1 = models.IntegerField(blank=True, null=True)
	kartet_index2 = models.IntegerField(blank=True, null=True)
	kartet_index3 = models.IntegerField(blank=True, null=True)
	kartet_index4 = models.IntegerField(blank=True, null=True)
	kartet_index5 = models.IntegerField(blank=True, null=True)
	kartet_index6 = models.IntegerField(blank=True, null=True)
	kartet_index7 = models.IntegerField(blank=True, null=True)
	kartet_index8 = models.IntegerField(blank=True, null=True)

	def index_list(self):
		return [self.kartet_index1, self.kartet_index2, self.kartet_index3, self.kartet_index4, self.kartet_index5, self.kartet_index6, self.kartet_index7, self.kartet_index8]

	class Meta:
		db_table = 'honne_index_results'

class HonneTypeResult(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_type_results',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_type_results',
	    blank=True,
	    null=True
	)
	evaluation_period = models.ForeignKey(
	    HonneEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='honne_type_results',
	    blank=True,
	    null=True
	)
	kartet_type_a = models.IntegerField(blank=True, null=True)
	kartet_type_b = models.IntegerField(blank=True, null=True)
	kartet_type_c = models.IntegerField(blank=True, null=True)
	kartet_type_d = models.IntegerField(blank=True, null=True)
	flg_finished = models.BooleanField(default=False)

	class Meta:
		db_table = 'honne_type_results'

# SELFCHECK
class SelfcheckQuestion(models.Model):
	question = models.TextField()
	sort_no = models.IntegerField(blank=True, null=True)
	category_id = models.IntegerField(
			blank=True,
			null=True,
			choices=[
				(1, '決断力'), #square
				(2, '専門性'), #circle
				(3, '自己管理'), #triangle
				(4, '広報力'), #circle
				(5, '連携力'), #square
				(6, '人間関係'), #triangle
				(7, '患者対応'), #square
				(8, 'チームワーク力'), #triangle
				(9, '総合管理'), #circle
				(10, '理念浸透'), #circle
				(11, '自己啓発'), #triangle
				(12, '思考'), #square
			]
	    )
	class Meta:
		db_table = 'selfcheck_questions'

	def __str__(self):
		return str(self.question)

class SelfcheckEvaluationPeriod(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_evaluation_periods',
	    blank=True,
	    null=True
	)
	evaluation_name = models.CharField(max_length=255, verbose_name='評価名')
	evaluation_start = models.DateField(blank=True, null=True, verbose_name='評価開始時間')
	evaluation_end = models.DateField(blank=True, null=True, verbose_name='評価終了時間')
	selfcheck_questions = models.ManyToManyField(
		SelfcheckQuestion,
	    related_name='selfcheck_evaluation_periods',
	    blank=True,
	    verbose_name = 'SELFCHECK質問'
	)

	class Meta:
		db_table = 'selfcheck_evaluation_periods'
		verbose_name = 'SELFCHECK 評価期間'
		verbose_name_plural = 'SELFCHECK 評価期間'

	def __str__(self):
		return f"{self.evaluation_name}"

class SelfcheckAnswerResult(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_results',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_results',
	    blank=True,
	    null=True
	)
	selfcheck_question = models.ForeignKey(
	    SelfcheckQuestion,
	    on_delete=models.CASCADE,
	    related_name='selfcheck_results'
	)
	evaluation_period = models.ForeignKey(
	    SelfcheckEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_answer_results',
	    blank=True,
	    null=True
	)
	selfcheck_answer = models.IntegerField(blank=True, null=True)
	selfcheck_answer_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'selfcheck_answer_results'

class SelfcheckIndexResult(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_index_results',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_index_results',
	    blank=True,
	    null=True
	)
	evaluation_period = models.ForeignKey(
	    SelfcheckEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_index_results',
	    blank=True,
	    null=True
	)
	selfcheck_index1 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index2 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index3 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index4 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index5 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index6 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index7 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index8 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index9 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index10 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index11 = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_index12 = models.IntegerField(blank=True, null=True, default=0)

	def index_list(self):
		return [self.selfcheck_index1, self.selfcheck_index2, self.selfcheck_index3, self.selfcheck_index4, self.selfcheck_index5, self.selfcheck_index6, self.selfcheck_index7, self.selfcheck_index8, self.selfcheck_index9, self.selfcheck_index10, self.selfcheck_index11, self.selfcheck_index12]

	class Meta:
		db_table = 'selfcheck_index_results'

class SelfcheckTypeResult(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_type_results',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_type_results',
	    blank=True,
	    null=True
	)
	evaluation_period = models.ForeignKey(
	    SelfcheckEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='selfcheck_type_results',
	    blank=True,
	    null=True
	)
	selfcheck_circl = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_square = models.IntegerField(blank=True, null=True, default=0)
	selfcheck_traiangle = models.IntegerField(blank=True, null=True, default=0)
	flg_finished = models.BooleanField(default=False)

	def type_list(self):
		return [self.selfcheck_circl, self.selfcheck_square, self.selfcheck_traiangle]

	class Meta:
		db_table = 'selfcheck_type_results'

# BONKNOW
class ResponsQuestion(models.Model):
	class Meta:
		verbose_name = 'Respons question'

	question = models.TextField()
	sort_no = models.IntegerField(blank=True, null=True)
	question_type = models.CharField(
		max_length=1,
		null=True,
		choices=[
			('1', 'Logic'),
			('2', 'Sense'),
		]
	)
	apply_start_date = models.DateField(blank=True, null=True)
	apply_end_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'respons_questions'

	def __str__(self):
		return str(self.question)

class ThinkQuestion(models.Model):
	class Meta:
		verbose_name = 'Think question'

	question = models.TextField()
	sort_no = models.IntegerField(blank=True, null=True)
	question_type = models.CharField(
		max_length=1,
		null=True,
		choices=[
			('1', 'Must'),
			('2', 'Want'),
		]
	)
	apply_start_date = models.DateField(blank=True, null=True)
	apply_end_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'think_questions'

	def __str__(self):
		return str(self.question)

class BonknowEvaluationPeriod(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='bonknow_evaluation_periods',
	    blank=True,
	    null=True
	)
	evaluation_name = models.CharField(max_length=255, verbose_name='評価名')
	evaluation_start = models.DateField(blank=True, null=True, verbose_name='評価開始時間')
	evaluation_end = models.DateField(blank=True, null=True, verbose_name='評価終了時間')
	respons_questions = models.ManyToManyField(
		ResponsQuestion,
	    related_name='bonknow_evaluation_periods',
	    blank=True,
	    verbose_name='RESPONS質問'
	)
	think_questions = models.ManyToManyField(
		ThinkQuestion,
	    related_name='bonknow_evaluation_periods',
	    blank=True,
	    verbose_name='THINK質問'
	)

	class Meta:
		db_table = 'bonknow_evaluation_periods'
		verbose_name = 'BONKNOW 評価期間'
		verbose_name_plural = 'BONKNOW 評価期間'

	def __str__(self):
		return f"{self.evaluation_name}"

class ResponsAnswer(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='respons_answers',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='respons_answers',
	    blank=True,
	    null=True
	)
	respons_question = models.ForeignKey(
	    ResponsQuestion,
	    on_delete=models.CASCADE,
	    related_name='respons_answers'
	)
	evaluation_period = models.ForeignKey(
	    BonknowEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='respons_answers',
	    blank=True,
	    null=True
	)
	answer = models.IntegerField(blank=True, null=True)
	answer_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'respons_answers'

class ThinkAnswer(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='think_answers',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='think_answers',
	    blank=True,
	    null=True
	)
	think_question = models.ForeignKey(
	    ThinkQuestion,
	    on_delete=models.CASCADE,
	    related_name='think_answers'
	)
	evaluation_period = models.ForeignKey(
	    BonknowEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='think_answers',
	    blank=True,
	    null=True
	)
	answer = models.IntegerField(blank=True, null=True)
	answer_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'think_answers'

class ResponsResult(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='respons_results',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='respons_results',
	    blank=True,
	    null=True
	)
	evaluation_period = models.ForeignKey(
	    BonknowEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='respons_results',
	    blank=True,
	    null=True
	)
	logic = models.FloatField(blank=True, null=True, default=0)
	sense = models.FloatField(blank=True, null=True, default=0)
	review_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'respons_results'

class ThinkResult(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='think_results',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='think_results',
	    blank=True,
	    null=True
	)
	evaluation_period = models.ForeignKey(
	    BonknowEvaluationPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='think_results',
	    blank=True,
	    null=True
	)
	must = models.FloatField(blank=True, null=True, default=0)
	want = models.FloatField(blank=True, null=True, default=0)
	review_date = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'think_results'

# MANDARA
class MandaraPeriod(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='mandara_periods',
	    blank=True,
	    null=True
	)
	start_date = models.DateField(verbose_name="評価開始時間")
	end_date = models.DateField(verbose_name="評価終了時間")

	class Meta:
		db_table = 'mandara_periods'
		verbose_name = 'MANDARA 評価期間'
		verbose_name_plural = 'MANDARA 評価期間'
		
	def __str__(self):
		return str("")

	def clean(self):
		if self.start_date > self.end_date:
			raise ValidationError("日付が間違っています。")
		check_time = self.__class__.objects.filter(company_id=self.company_id,end_date__gte=self.start_date,start_date__lte=self.end_date).exists()
		if check_time is True:
			raise ValidationError("日付が重複しています。")
		

		
class MandaraBase(models.Model):
	company = models.ForeignKey(
	    Company,
	    on_delete=models.DO_NOTHING,
	    related_name='mandara_base',
	    blank=True,
	    null=True
	)
	user = models.ForeignKey(
	    User,
	    on_delete=models.DO_NOTHING,
	    related_name='mandara_base',
	    blank=True,
	    null=True
	)
	mandara_period = models.ForeignKey(
	    MandaraPeriod,
	    on_delete=models.DO_NOTHING,
	    related_name='mandara_base',
	    blank=True,
	    null=True
	)
	total_mission = models.CharField(max_length=20, blank=True, null=True)

	A_keyword = models.CharField(max_length=20, blank=True, null=True)
	A_dueto = models.TextField(blank=True, null=True)
	A_result = models.IntegerField(default=0)
	A1_content = models.CharField(max_length=20)
	A2_content = models.CharField(max_length=20)
	A3_content = models.CharField(max_length=20)
	A4_content = models.CharField(max_length=20)
	A5_content = models.CharField(max_length=20)
	A6_content = models.CharField(max_length=20)
	A7_content = models.CharField(max_length=20)
	A8_content = models.CharField(max_length=20)

	B_keyword = models.CharField(max_length=20, blank=True, null=True)
	B_dueto = models.TextField(blank=True, null=True)
	B_result = models.IntegerField(default=0)
	B1_content = models.CharField(max_length=20)
	B2_content = models.CharField(max_length=20)
	B3_content = models.CharField(max_length=20)
	B4_content = models.CharField(max_length=20)
	B5_content = models.CharField(max_length=20)
	B6_content = models.CharField(max_length=20)
	B7_content = models.CharField(max_length=20)
	B8_content = models.CharField(max_length=20)

	C_keyword = models.CharField(max_length=20, blank=True, null=True)
	C_dueto = models.TextField(blank=True, null=True)
	C_result = models.IntegerField(default=0)
	C1_content = models.CharField(max_length=20)
	C2_content = models.CharField(max_length=20)
	C3_content = models.CharField(max_length=20)
	C4_content = models.CharField(max_length=20)
	C5_content = models.CharField(max_length=20)
	C6_content = models.CharField(max_length=20)
	C7_content = models.CharField(max_length=20)
	C8_content = models.CharField(max_length=20)

	D_keyword = models.CharField(max_length=20, blank=True, null=True)
	D_dueto = models.TextField(blank=True, null=True)
	D_result = models.IntegerField(default=0)
	D1_content = models.CharField(max_length=20)
	D2_content = models.CharField(max_length=20)
	D3_content = models.CharField(max_length=20)
	D4_content = models.CharField(max_length=20)
	D5_content = models.CharField(max_length=20)
	D6_content = models.CharField(max_length=20)
	D7_content = models.CharField(max_length=20)
	D8_content = models.CharField(max_length=20)

	E_keyword = models.CharField(max_length=20, blank=True, null=True)
	E_dueto = models.TextField(blank=True, null=True)
	E_result = models.IntegerField(default=0)
	E1_content = models.CharField(max_length=20)
	E2_content = models.CharField(max_length=20)
	E3_content = models.CharField(max_length=20)
	E4_content = models.CharField(max_length=20)
	E5_content = models.CharField(max_length=20)
	E6_content = models.CharField(max_length=20)
	E7_content = models.CharField(max_length=20)
	E8_content = models.CharField(max_length=20)

	F_keyword = models.CharField(max_length=20, blank=True, null=True)
	F_dueto = models.TextField(blank=True, null=True)
	F_result = models.IntegerField(default=0)
	F1_content = models.CharField(max_length=20)
	F2_content = models.CharField(max_length=20)
	F3_content = models.CharField(max_length=20)
	F4_content = models.CharField(max_length=20)
	F5_content = models.CharField(max_length=20)
	F6_content = models.CharField(max_length=20)
	F7_content = models.CharField(max_length=20)
	F8_content = models.CharField(max_length=20)

	G_keyword = models.CharField(max_length=20, blank=True, null=True)
	G_dueto = models.TextField(blank=True, null=True)
	G_result = models.IntegerField(default=0)
	G1_content = models.CharField(max_length=20)
	G2_content = models.CharField(max_length=20)
	G3_content = models.CharField(max_length=20)
	G4_content = models.CharField(max_length=20)
	G5_content = models.CharField(max_length=20)
	G6_content = models.CharField(max_length=20)
	G7_content = models.CharField(max_length=20)
	G8_content = models.CharField(max_length=20)

	H_keyword = models.CharField(max_length=20, blank=True, null=True)
	H_dueto = models.TextField(blank=True, null=True)
	H_result = models.IntegerField(default=0)
	H1_content = models.CharField(max_length=20, blank=True, null=True)
	H2_content = models.CharField(max_length=20, blank=True, null=True)
	H3_content = models.CharField(max_length=20, blank=True, null=True)
	H4_content = models.CharField(max_length=20, blank=True, null=True)
	H5_content = models.CharField(max_length=20, blank=True, null=True)
	H6_content = models.CharField(max_length=20, blank=True, null=True)
	H7_content = models.CharField(max_length=20, blank=True, null=True)
	H8_content = models.CharField(max_length=20, blank=True, null=True)
	flg_finished = models.BooleanField(default=False)
	field_stop = models.CharField(max_length=20, blank=True, null=True)

	def total_result(self):
			return self.A_result + self.B_result + self.C_result + self.D_result + self.E_result + self.F_result + self.G_result + self.H_result

	# def display_time(self):
	# 		return f'{self.start_YYYYMM[:4]}/{int(self.start_YYYYMM[4:])} ~ {self.end_YYYYMM[:4]}/{int(self.end_YYYYMM[4:])}'

	class Meta:
		db_table = 'mandara_base'
		# constraints = [
	    #     models.UniqueConstraint(fields=['user_id', 'company_id', 'start_YYYYMM', 'end_YYYYMM'], name='unique_mandara')
	    # ]

class MandaraProgress(models.Model):
	mandara_base = models.ForeignKey(
	    MandaraBase,
	    on_delete=models.DO_NOTHING,
	    related_name='mandara_progress',
	    blank=True,
	    null=True
	)
	date = models.DateField(blank=True, null=True)

	A1_result = models.IntegerField(default=0)
	A2_result = models.IntegerField(default=0)
	A3_result = models.IntegerField(default=0)
	A4_result = models.IntegerField(default=0)
	A5_result = models.IntegerField(default=0)
	A6_result = models.IntegerField(default=0)
	A7_result = models.IntegerField(default=0)
	A8_result = models.IntegerField(default=0)

	B1_result = models.IntegerField(default=0)
	B2_result = models.IntegerField(default=0)
	B3_result = models.IntegerField(default=0)
	B4_result = models.IntegerField(default=0)
	B5_result = models.IntegerField(default=0)
	B6_result = models.IntegerField(default=0)
	B7_result = models.IntegerField(default=0)
	B8_result = models.IntegerField(default=0)

	C1_result = models.IntegerField(default=0)
	C2_result = models.IntegerField(default=0)
	C3_result = models.IntegerField(default=0)
	C4_result = models.IntegerField(default=0)
	C5_result = models.IntegerField(default=0)
	C6_result = models.IntegerField(default=0)
	C7_result = models.IntegerField(default=0)
	C8_result = models.IntegerField(default=0)

	D1_result = models.IntegerField(default=0)
	D2_result = models.IntegerField(default=0)
	D3_result = models.IntegerField(default=0)
	D4_result = models.IntegerField(default=0)
	D5_result = models.IntegerField(default=0)
	D6_result = models.IntegerField(default=0)
	D7_result = models.IntegerField(default=0)
	D8_result = models.IntegerField(default=0)

	E1_result = models.IntegerField(default=0)
	E2_result = models.IntegerField(default=0)
	E3_result = models.IntegerField(default=0)
	E4_result = models.IntegerField(default=0)
	E5_result = models.IntegerField(default=0)
	E6_result = models.IntegerField(default=0)
	E7_result = models.IntegerField(default=0)
	E8_result = models.IntegerField(default=0)

	F1_result = models.IntegerField(default=0)
	F2_result = models.IntegerField(default=0)
	F3_result = models.IntegerField(default=0)
	F4_result = models.IntegerField(default=0)
	F5_result = models.IntegerField(default=0)
	F6_result = models.IntegerField(default=0)
	F7_result = models.IntegerField(default=0)
	F8_result = models.IntegerField(default=0)

	G1_result = models.IntegerField(default=0)
	G2_result = models.IntegerField(default=0)
	G3_result = models.IntegerField(default=0)
	G4_result = models.IntegerField(default=0)
	G5_result = models.IntegerField(default=0)
	G6_result = models.IntegerField(default=0)
	G7_result = models.IntegerField(default=0)
	G8_result = models.IntegerField(default=0)

	H1_result = models.IntegerField(default=0)
	H2_result = models.IntegerField(default=0)
	H3_result = models.IntegerField(default=0)
	H4_result = models.IntegerField(default=0)
	H5_result = models.IntegerField(default=0)
	H6_result = models.IntegerField(default=0)
	H7_result = models.IntegerField(default=0)
	H8_result = models.IntegerField(default=0)

	def sum_result(self):
		return self.A1_result + self.B1_result + self.C1_result + self.D1_result + self.E1_result + self.F1_result + self.G1_result + self.H1_result + self.A2_result + self.B2_result + self.C2_result + self.D2_result + self.E2_result + self.F2_result + self.G2_result + self.H2_result + self.A3_result + self.B3_result + self.C3_result + self.D3_result + self.E3_result + self.F3_result + self.G3_result + self.H3_result + self.A4_result + self.B4_result + self.C4_result + self.D4_result + self.E4_result + self.F4_result + self.G4_result + self.H4_result + self.A5_result + self.B5_result + self.C5_result + self.D5_result + self.E5_result + self.F5_result + self.G5_result + self.H5_result + self.A6_result + self.B6_result + self.C6_result + self.D6_result + self.E6_result + self.F6_result + self.G6_result + self.H6_result + self.A7_result + self.B7_result + self.C7_result + self.D7_result + self.E7_result + self.F7_result + self.G7_result + self.H7_result + self.A8_result + self.B8_result + self.C8_result + self.D8_result + self.E8_result + self.F8_result + self.G8_result + self.H8_result
	class Meta:
		db_table = 'mandara_progress'
		constraints = [
	        models.UniqueConstraint(fields=['mandara_base_id', 'date'], name='unique_mandara_progress')
	    ]