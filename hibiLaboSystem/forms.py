from django import forms
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
import datetime
from . import models, fields

User = get_user_model()

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email','username')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = ""

            if field.label == '姓':
                field.widget.attrs['autofocus'] = ""
                field.widget.attrs['placeholder'] = 'なかしま'
            elif field.label == '名':
                field.widget.attrs['placeholder'] = 'こういち'
            elif field.label == 'メールアドレス':
                field.widget.attrs['placeholder'] = '***@domain.com'

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'username')

    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = ""

class PasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class WorkInfoUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('preferred_day', 'preferred_day2',  'preferred_day3',  'preferred_day4',   'preferred_day5',  'preferred_day6',  'preferred_day7',  'preferred_hour', 'preferred_hour2', 'preferred_hour3', 'preferred_hour4', 'preferred_hour5', 'preferred_hour6', 'preferred_hour7')

    #　日別
    preferred_day = forms.BooleanField(
        required=False,
        initial=False,
        help_text='希望するならチェック',
    )
    preferred_hour = forms.ChoiceField(
        required=False,
        choices=(
            ("0", '-'), (1, '①09:00～13:00'), (2, '②17:00～22:00'), (3, '③22:00～06:00')
        ),
        widget=forms.Select(attrs={'class': 'form'})
    )
    preferred_day2 = forms.BooleanField(
        initial=False,
        help_text='希望するならチェック',
        required=False,
    )
    preferred_hour2 = forms.ChoiceField(
        required=False,
        choices=(
            ("0", '-'), (1, '①09:00～13:00'), (2, '②17:00～22:00'), (3, '③22:00～06:00')
        ),
        widget=forms.Select(attrs={'class': 'form'})
    )
    preferred_day3 = forms.BooleanField(
        initial=False,
        help_text='希望するならチェック',
        required=False,
    )
    preferred_hour3 = forms.ChoiceField(
        required=False,
        choices=(
            ("0", '-'), (1, '①09:00～13:00'), (2, '②17:00～22:00'), (3, '③22:00～06:00')
        ),
        widget=forms.Select(attrs={'class': 'form'})
    )
    preferred_day4 = forms.BooleanField(
        initial=False,
        help_text='希望するならチェック',
        required=False,
    )
    preferred_hour4 = forms.ChoiceField(
        required=False,
        choices=(
            ("0", '-'), (1, '①09:00～13:00'), (2, '②17:00～22:00'), (3, '③22:00～06:00')
        ),
        widget=forms.Select(attrs={'class': 'form'})
    )
    preferred_day5 = forms.BooleanField(
        initial=False,
        help_text='希望するならチェック',
        required=False,
    )
    preferred_hour5 = forms.ChoiceField(
        required=False,
        choices=(
            ("0", '-'), (1, '①09:00～13:00'), (2, '②17:00～22:00'), (3, '③22:00～06:00')
        ),
        widget=forms.Select(attrs={'class': 'form'})
    )
    preferred_day6 = forms.BooleanField(
        initial=False,
        help_text='希望するならチェック',
        required=False,
    )
    preferred_hour6 = forms.ChoiceField(
        required=False,
        choices=(
            ("0", '-'), (1, '①09:00～13:00'), (2, '②17:00～22:00'), (3, '③22:00～06:00')
        ),
        widget=forms.Select(attrs={'class': 'form'})
    )
    preferred_day7 = forms.BooleanField(
        initial=False,
        help_text='希望するならチェック',
        required=False,
    )
    preferred_hour7 = forms.ChoiceField(
        required=False,
        choices=(
            ("0", '-'), (1, '①09:00～13:00'), (2, '②17:00～22:00'), (3, '③22:00～06:00')
        ),
        widget=forms.Select(attrs={'class': 'form'})
    )

class HonneForm(forms.Form):
    flg_finished = forms.BooleanField(
        initial=False,
        label='提出する',
        required=False,
        help_text='提出する'
    )

class SelfcheckForm(forms.Form):
    flg_finished = forms.BooleanField(
        initial=False,
        label='提出する',
        required=False,
        help_text='提出する'
    )

''' 一次的に評価対象月などを静的に出力するためのフォーム'''
class HonneEvaluationUnitForm(forms.Form):
    # 評価対象年月の選択
    evaluation_unit = forms.ModelChoiceField(
        empty_label='----',
        label='評価対象年月',
        required=True,
        widget=forms.Select(attrs={'class': 'form'}),
        queryset=models.HonneEvaluationPeriod.objects.none()
    )

    # 評価対象社員の選択
    user_id = forms.ModelChoiceField(
        empty_label='全社員',
        label='対象社員',
        required=False,
        widget=forms.Select(attrs={'class': 'form'}),
        queryset=models.User.objects.none()
    )

    def __init__(self, request, *args, **kwargs):
        super(HonneEvaluationUnitForm, self).__init__(*args, **kwargs)
        queryset = models.User.objects.all()
        queryset_evaluation = models.HonneEvaluationPeriod.objects.all()
        if request.user:
            queryset = queryset.filter(company_id=request.user.company_id)
            queryset_evaluation = queryset_evaluation.filter(company_id=request.user.company_id)
        self.fields['user_id'].queryset = queryset
        self.fields['evaluation_unit'].queryset = queryset_evaluation

class SelfcheckEvaluationUnitForm(forms.Form):
    # 評価対象年月の選択
    evaluation_unit = forms.ModelChoiceField(
        empty_label='----',
        label='評価対象年月',
        required=True,
        widget=forms.Select(attrs={'class': 'form'}),
        queryset=models.SelfcheckEvaluationPeriod.objects.none()
    )

    # 評価対象社員の選択
    user_id = forms.ModelChoiceField(
        empty_label='全社員',
        label='対象社員',
        required=False,
        widget=forms.Select(attrs={'class': 'form'}),
        queryset=models.User.objects.none()
    )

    def __init__(self, request, *args, **kwargs):
        super(SelfcheckEvaluationUnitForm, self).__init__(*args, **kwargs)
        queryset = models.User.objects.all()
        queryset_evaluation = models.SelfcheckEvaluationPeriod.objects.all()
        if request.user:
            queryset = queryset.filter(company_id=request.user.company_id)
            queryset_evaluation = queryset_evaluation.filter(company_id=request.user.company_id)
        self.fields['user_id'].queryset = queryset
        self.fields['evaluation_unit'].queryset = queryset_evaluation
        self.fields['user_id'].queryset = queryset

class BonknowForm(forms.Form):
    start = forms.ChoiceField(
        widget=fields.MonthYearSelectWidget(),
        required=True
    )

    end = forms.ChoiceField(
        widget=fields.MonthYearSelectWidget(),
        required=True
    )

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()