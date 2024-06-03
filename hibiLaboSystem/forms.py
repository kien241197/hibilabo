from django import forms
from .models import *
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
import datetime
from . import models, fields
from .enums import *
import PIL
from django.utils.safestring import mark_safe

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
            queryset = models.User.objects.filter(company_id=request.user.company.id)
            #Company_Supervisor
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                if request.user.branch:
                    queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)
                else:
                    queryset = queryset

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = queryset
            
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
            queryset = models.User.objects.filter(company_id=request.user.company.id)
            #Company_Supervisor 
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                if request.user.branch:
                    queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)
                else:
                    queryset = queryset

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = queryset
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
    csv_file = forms.FileField(widget=forms.FileInput(attrs={'accept':'.csv, text/csv'}))

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
                'placeholder': 'ドラ１\n8 球団',
                'rows':0,
                'tabindex':"1"
            }
        )
    )

    A_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...',
                'tabindex':"3"
                
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
                'rows':0,
                'tabindex':"4"
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
                'placeholder': 'あいさつ',
                'rows':0,
                'tabindex': '19'
            }
        )
    )
    A2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': 'ゴミ拾い',
                'rows':0,
                'tabindex': '20'
            }
        )
    )
    A3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '部屋掃除',
                'rows':0,
                'tabindex': '21'
            }
        )
    )
    A4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '12',
                'placeholder': '審判さんへの\n態度'
            }
        )
    )
    A5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '23',
                'placeholder': '本を読む'
            }
        )
    )
    A6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '24',
                'placeholder': '応援される\n人間になる'
            }
        )
    )
    A7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '25',
                'placeholder': 'プラス思考'
            }
        )
    )
    A8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '26',
                'placeholder': '道具を\n大切に使う'
            }
        )
    )

    B_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...',
                'tabindex': "5",
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
                'rows':0,
                'tabindex': "6"
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
                'placeholder': 'はっきりと\nした目標\n目的を持つ',
                'rows':0,
                'tabindex': '27'
            }
        )
    )
    B2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '一喜一憂\nしない',
                'rows':0,
                'tabindex': '28'
            }
        )
    )
    B3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '頭は冷静に\n心は熱く',
                'rows':0,
                'tabindex': '29'
            }
        )
    )
    B4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '30',
                'placeholder': '雰囲気に\n流されない'
            }
        )
    )
    B5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '31',
                'placeholder': '仲間を\n思いやる心'
            }
        )
    )
    B6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '32',
                'placeholder' : '勝利への\n執念'
            }
        )
    )
    B7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '33',
                'placeholder': '波を\nつくらない'
            }
        )
    )
    B8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '34',
                'placeholder': 'ピンチに\n強い'
            }
        )
    )

    C_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...',
                'tabindex': '7'
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
                'rows':0,
                'tabindex': '8'
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
                'placeholder': 'インステップ\n改善',
                'rows':0,
                'tabindex': '35'
            }
        )
    )
    C2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '体幹強化',
                'rows':0,
                'tabindex': '36'
            }
        )
    )
    C3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '軸を\nぶらさない',
                'rows':0,
                'tabindex': '37'
            }
        )
    )
    C4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '38',
                'placeholder': '不安を\nなくす'
            }
        )
    )
    C5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '39',
                'placeholder': 'メンタ\nコントロール\nをする'
            }
        )
    )
    C6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '40',
                'placeholder': '体を開かない'
            }
        )
    )
    C7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '41',
                'placeholder': '下肢の\n強化'
            }
        )
    )
    C8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '42',
                'placeholder': 'リリース\nポイントの\n安定'
            }
        )
    )

    D_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...',
                'tabindex': '9'
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
                'rows':0,
                'tabindex': '10'
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
                'placeholder': '軸でまわる',
                'rows':0,
                'tabindex': '43'
            }
        )
    )
    D2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '下肢の強化',
                'rows':0,
                'tabindex': '44'
            }
        )
    )
    D3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '体重增加',
                'rows':0,
                'tabindex': '45'
            }
        )
    )
    D4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '46',
                'placeholder': '肩周りの\n強化'
            }
        )
    )
    D5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '47',
                'placeholder': 'ピッチングを\n増やす'
            }
        )
    )
    D6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '48',
                'placeholder': 'ライナー\nキャッチボール'
            }
        )
    )
    D7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '49',
                'placeholder': '可動域'
            }
        )
    )
    D8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '50',
                'placeholder': '体幹強化'
            }
        )
    )

    E_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...',
                'tabindex': '11'
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
                'rows':0,
                'tabindex': '12'
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
                'placeholder': '感性',
                'rows':0,
                'tabindex': '51'
            }
        )
    )
    E2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '愛される\n人間',
                'rows':0,
                'tabindex': '52'
            }
        )
    )
    E3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '計画性',
                'rows':0,
                'tabindex': '53'
            }
        )
    )
    E4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '54',
                'placeholder': '感謝'
            }
        )
    )
    E5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '55',
                'placeholder': '継続力'
            }
        )
    )
    E6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '56',
                'placeholder': '信頼される\n人間'
            }
        )
    )
    E7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '57',
                'placeholder': '礼儀'
            }
        )
    )
    E8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '58',
                'placeholder': '思いやり'
            }
        )
    )

    F_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...',
                'tabindex': '13'
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
                'rows':0,
                'tabindex': '14'
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
                'placeholder': '体のケア',
                'rows':0,
                'tabindex': '59'
            }
        )
    )
    F2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': 'サプリメント\nを飲む',
                'rows':0,
                'tabindex': '60'
            }
        )
    )
    F3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': 'FSQ\n90kg',
                'rows':0,
                'tabindex': '61'
            }
        )
    )
    F4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': 'RSQ\n130kg',
                'rows':0,
                'tabindex': '62'
            }
        )
    )
    F5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '63',
                'placeholder': '食事\n夜7杯 朝3杯'
            }
        )
    )
    F6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '64',
                'placeholder': '可動性'
            }
        )
    )
    F7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '65',
                'placeholder': 'スタミナ'
            }
        )
    )
    F8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '66',   
                'placeholder' : '柔軟性'
            }
        )
    )

    G_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...',
                'tabindex': '15'
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
                'rows':0,
                'tabindex': '16'
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
                'placeholder': '角度を\nつける',
                'rows':0,
                'tabindex': '67'
            }
        )
    )
    G2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': '上から\nボールを\nたたく',
                'rows':0,
                'tabindex': '68'
            }
        )
    )
    G3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': 'リストの\n強化',
                'rows':0,
                'tabindex': '69'
            }
        )
    )
    G4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '70',
                'placeholder': '下半身\n主導'
            }
        )
    )
    G5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '71',
                'placeholder': '可動域'
            }
        )
    )
    G6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '72',
                'placeholder': '回転数\nアップ'
            }
        )
    )
    G7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '73',
                'placeholder': 'ボールを\n軸で\nリリース'
            }
        )
    )
    G8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '74',
                'placeholder': '力まない'
            }
        )
    )

    H_keyword = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "input-value-tab",
                'placeholder': '20文字以内で入力してください...',
                'tabindex': '17'
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
                'rows':0,
                'tabindex': '18'
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
                'placeholder': 'カウントボールを増やす',
                'rows':0,
                'tabindex': '75'
            }
        )
    )
    H2_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': 'フォーク完成',
                'rows':0,
                'tabindex': '76'
            }
        )
    )
    H3_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'placeholder': 'スライダーの\nキレ',
                'rows':0,
                'tabindex': '77'
            }
        )
    )
    H4_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '78',
                'placeholder': '左打者\nへの決め球'
            }
        )
    )
    H5_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '79',
                'placeholder': '奥行き\nのイメージ'
            }
        )
    )
    H6_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '80',
                'placeholder': 'ストライクから\nボールに投げる\nコントロール'
            }
        )
    )
    H7_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '81',
                'placeholder': 'ストレートと\n同じフォームで\n投げる'
            }
        )
    )
    H8_content = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': "input-table",
                'rows':0,
                'tabindex': '82',
                'placeholder': '遅く落差\nのあるカーブ'
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
            queryset = models.User.objects.filter(company_id=request.user.company.id)
            #Company_Supervisor 
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                if request.user.branch:
                    queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)
                else:
                    queryset = queryset

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = queryset
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
            queryset = models.User.objects.filter(company_id=request.user.company.id)
            #Company_Supervisor 
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                if request.user.branch:
                    queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)
                else:
                    queryset = queryset

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = queryset
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
            queryset = models.User.objects.filter(company_id=request.user.company.id)
            #Company_Supervisor 
            if request.user.role.role == RoleEnum.Company_SuperVisor.value:
                if request.user.branch:
                    queryset = models.User.objects.filter(branch=request.user.branch.id, company_id=request.user.company.id)
                else:
                    queryset = queryset

            # Company_Admin
            if request.user.role.role == RoleEnum.Company_Admin.value:
                queryset = queryset

            queryset_evaluation = queryset_evaluation.filter(company_id=request.user.company_id)
        self.fields['user_id'].queryset = queryset
        self.fields['evaluation_unit'].queryset = queryset_evaluation
        
class TeamConceptForm(forms.Form):
    class Meta:
        model= models.Company
        fields = "__all__"


class CheckboxSelectMultipleWithSelectAll(forms.CheckboxSelectMultiple):
    class Media:
        js = ('js/select_all.js',)  
