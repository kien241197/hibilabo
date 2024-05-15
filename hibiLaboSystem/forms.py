from django import forms
from .models import *
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
import datetime
from . import models, fields
from .enums import *
import PIL

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
        fields = ('last_name', 'first_name', 'email', 'username', 'image')

    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

            if field.label != "アバター":
                field.widget.attrs['required'] = ""
            else:
                field.widget.attrs['required'] = False

    def save(self):
        s = super(UserUpdateForm, self).save()
        if s.image:
            image = PIL.Image.open(s.image)
            cropped_image = image.crop((0, 1, image.width, image.height))
            resized_image = cropped_image.resize((460, 430), PIL.Image.Resampling.LANCZOS)
            resized_image.save(s.image.path)
        return s

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

class BonknowSheetForm(forms.Form):
    flg_finished = forms.BooleanField(
        initial=False,
        label='提出する',
        required=False,
        help_text='提出する'
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
        queryset_evaluation = models.HonneEvaluationPeriod.objects.all()
        if request.user:
            #Company_Supervisor 
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = models.User.objects.filter(company_id=request.user.company.id)
            
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

        queryset_evaluation = models.SelfcheckEvaluationPeriod.objects.all()
        if request.user:
            #Company_Supervisor 
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = models.User.objects.filter(company_id=request.user.company.id)
            # queryset = queryset.filter(company_id=request.user.company_id)
            queryset_evaluation = queryset_evaluation.filter(company_id=request.user.company_id)
        self.fields['user_id'].queryset = queryset
        self.fields['evaluation_unit'].queryset = queryset_evaluation

class BonknowForm(forms.Form):

    evaluation_unit = forms.ModelChoiceField(
        empty_label='----',
        label='評価対象年月',
        required=True,
        widget=forms.Select(attrs={'class': 'form'}),
        queryset=models.BonknowEvaluationPeriod.objects.none()
    )

    def __init__(self, request, *args, **kwargs):
        super(BonknowForm, self).__init__(*args, **kwargs)
        queryset_evaluation = models.BonknowEvaluationPeriod.objects.all()
        self.fields['evaluation_unit'].queryset = queryset_evaluation

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class MandaraCreateForm(forms.ModelForm):
    class Meta:
        model = models.MandaraBase
        fields = "__all__"
        exclude = ["user", "company"]

    # start_YYYYMM = forms.ChoiceField(
    #     widget=fields.MandaraYearSelectWidget(),
    #     required=False
    # )

    # end_YYYYMM = forms.ChoiceField(
    #     widget=fields.MandaraYearSelectWidget(),
    #     required=False
    # )

    total_mission = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-value-score",
                'placeholder': 'ドラ 18 球団 ',
                'rows':0
            }
        )
    )

    A_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...'
            }
        )
    )
    A_dueto = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table input-table-desc",
                'placeholder': '記述...!',
                'rows':0
            }
        )
    )
    A_result = forms.IntegerField(required=False)
    A1_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例体のケア',
                'rows':0
            }
        )
    )
    A2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    A3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    A4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    A5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    A6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    A7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    A8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )

    B_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...'
            }
        )
    )
    B_dueto = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table input-table-desc",
                'placeholder': '記述...!',
                'rows':0
            }
        )
    )
    B_result = forms.IntegerField(required=False)
    B1_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    B2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    B3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    B4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    B5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    B6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    B7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    B8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )

    C_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...'
            }
        )
    )
    C_dueto = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table input-table-desc",
                'placeholder': '記述...!',
                'rows':0
            }
        )
    )
    C_result = forms.IntegerField(required=False)
    C1_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    C2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    C3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    C4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    C5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    C6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    C7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    C8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )

    D_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...'
            }
        )
    )
    D_dueto = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table input-table-desc",
                'placeholder': '記述...!',
                'rows':0
            }
        )
    )
    D_result = forms.IntegerField(required=False)
    D1_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    D2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    D3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    D4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    D5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    D6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    D7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    D8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )

    E_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...'
            }
        )
    )
    E_dueto = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table input-table-desc",
                'placeholder': '記述...!',
                'rows':0
            }
        )
    )
    E_result = forms.IntegerField(required=False)
    E1_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    E2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    E3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    E4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    E5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    E6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    E7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    E8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )

    F_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...'
            }
        )
    )
    F_dueto = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table input-table-desc",
                'placeholder': '記述...!',
                'rows':0
            }
        )
    )
    F_result = forms.IntegerField(required=False)
    F1_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    F2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    F3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    F4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    F5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    F6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    F7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    F8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )

    G_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...'
            }
        )
    )
    G_dueto = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table input-table-desc",
                'placeholder': '記述...!',
                'rows':0
            }
        )
    )
    G_result = forms.IntegerField(required=False)
    G1_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    G2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    G3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    G4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    G5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    G6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    G7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    G8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )

    H_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...'
            }
        )
    )
    H_dueto = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table input-table-desc",
                'placeholder': '記述...!',
                'rows':0
            }
        )
    )
    H_result = forms.IntegerField(required=False)
    H1_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    H2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    H3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '記入例',
                'rows':0
            }
        )
    )
    H4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    H5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    H6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    H7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    H8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0
            }
        )
    )
    field_stop = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "hidden",
            }
        )
    )

class MandaraCompleteForm(forms.Form):
    def __init__(self, company_id, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically set the widget choices based on company_id
        start_periods = MandaraPeriod.objects.filter(
            company_id=company_id
        ).order_by('start_date')

        end_periods = MandaraPeriod.objects.filter(
            company_id=company_id
        ).order_by('start_date')

        start_choices = [(period.start_date, period.display_time_start) for period in start_periods]
        end_choices = [(period.start_date, period.display_time_start) for period in end_periods]

        self.fields['start'] = forms.ChoiceField(
            choices=[('', '----')] + start_choices,
            widget=fields.MandaraMonthYearSelectWidget(company_id=company_id),
        )

        self.fields['end'] = forms.ChoiceField(
            choices=[('', '----')] + end_choices,
            widget=fields.MandaraMonthYearSelectWidget(company_id=company_id),
        )


class MandaraChartForm(forms.Form):

    # 評価対象社員の選択
    user_id = forms.ModelChoiceField(
        empty_label='全社員',
        label='対象社員',
        required=False,
        widget=forms.Select(attrs={'class': 'form font-weight-bold'}),
        queryset=models.User.objects.none()
    )

    def __init__(self, request, *args, **kwargs):
        super(MandaraChartForm, self).__init__(*args, **kwargs)
        # queryset = models.User.objects.all()
        if request.user:
            #Company_Supervisor 
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = models.User.objects.filter(company_id=request.user.company.id)
        self.fields['user_id'].queryset = queryset

class MandaraForm(forms.Form):

    # 評価対象社員の選択
    user_id = forms.ModelChoiceField(
        empty_label='----',
        label='対象社員',
        required=True,
        widget=forms.Select(attrs={'class': 'form font-weight-bold'}),
        queryset=models.User.objects.none()
    )

    def __init__(self, request, *args, **kwargs):
        super(MandaraForm, self).__init__(*args, **kwargs)
        # queryset = models.User.objects.all()
        if request.user:
            #Company_Supervisor 
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = models.User.objects.filter(company_id=request.user.company.id)
        self.fields['user_id'].queryset = queryset

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = models.User
        exclude = ['is_superuser']

class WatasheetForm(forms.ModelForm):
    class Meta:
        model = models.WatasheetTypeResult
        fields = "__all__"

    flg_finished = forms.BooleanField(
        initial=False,
        label='提出する',
        required=False,
        help_text='提出する'
    )



class WatasheetTypeForm(forms.Form):

    # 評価対象年月の選択
    evaluation_unit = forms.ModelChoiceField(
        empty_label='----',
        label='評価対象年月',
        required=True,
        widget=forms.Select(attrs={'class': 'form'}),
        queryset=models.WatasheetEvaluationPeriod.objects.none()
    )

    # 評価対象社員の選択
    user_id = forms.ModelChoiceField(
        empty_label='----',
        label='対象社員',
        required=True,
        widget=forms.Select(attrs={'class': 'form'}),
        queryset=models.User.objects.none()
    )


    def __init__(self, request, *args, **kwargs):
        super(WatasheetTypeForm, self).__init__(*args, **kwargs)
        queryset_evaluation = models.WatasheetEvaluationPeriod.objects.all()
        
        if request.user:
            #Company_Supervisor 
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = models.User.objects.filter(company_id=request.user.company.id)

            queryset_evaluation = queryset_evaluation.filter(company_id=request.user.company_id)
        self.fields['user_id'].queryset = queryset
        self.fields['evaluation_unit'].queryset = queryset_evaluation
        
class TeamConceptForm(forms.Form):
    class Meta:
        model= models.Company
        fields = "__all__"


    
