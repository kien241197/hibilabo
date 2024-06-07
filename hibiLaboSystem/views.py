from . import forms, middlewares
from .models import *
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from pprint import pprint
from django.db.models import Q, Count, Prefetch, OuterRef, FilteredRelation, Sum
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View
from django.views.generic import ListView, CreateView, TemplateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import ExtractMonth, ExtractYear, ExtractDay, Coalesce
from .constants import SELFCHECK_ANSWER, CIRCL, SQUARE, TRAIANGLE
from django.utils.decorators import method_decorator
import calendar
import datetime
import pdb
import json
# use ReportLab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
# use wkhtmltopdf
from django.conf import settings
import os
from django.template.loader import get_template
import pdfkit
from django.db.models import Q, F
import jaconv

User = get_user_model()
wkhtml_to_pdf = os.path.join(
    settings.BASE_DIR, "wkhtmltopdf.exe")
# wkhtml_to_pdf = '/usr/bin/wkhtmltopdf'

def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        user_id = self.request.user.id
        if self.request.user.is_authenticated:
            company_id = self.request.user.company_id
            context["period_honne"] = HonneEvaluationPeriod.objects.all().filter(evaluation_start__lte=today,evaluation_end__gte=today,company_id=company_id).first()
            context["period_selfcheck"] = SelfcheckEvaluationPeriod.objects.all().filter(evaluation_start__lte=today,evaluation_end__gte=today,company_id=company_id).first()
            context["period_bonknow"] = BonknowEvaluationPeriod.objects.all().filter(evaluation_start__lte=today,evaluation_end__gte=today,company_id=company_id).first()
            context["period_watasheet"] = WatasheetEvaluationPeriod.objects.all().filter(evaluation_start__lte=today,evaluation_end__gte=today,company_id=company_id).first()
            if context["period_honne"] is not None:
                context['honne_type_result'] = HonneTypeResult.objects.filter(user_id=user_id, evaluation_period_id=context["period_honne"].id).first()

            if context["period_selfcheck"] is not None:
                context['selfcheck_type_result'] = SelfcheckTypeResult.objects.filter(user_id=user_id, evaluation_period_id=context["period_selfcheck"].id).first()
            
            if context["period_bonknow"] is not None:
                context['bonknow_type_result'] = ResponsResult.objects.filter(user_id=user_id, evaluation_period_id=context["period_bonknow"].id).first()
            
            if context["period_watasheet"] is not None: 
                context['watasheet_type_result'] = WatasheetTypeResult.objects.filter(user_id=user_id, evaluation_period_id=context["period_watasheet"].id).first()

            context["mandara"] = MandaraBase.objects.all().filter(Q(user_id=user_id) & Q(company_id=company_id) & (Q(mandara_period__start_date__gt=today))).order_by('mandara_period__start_date').first()
        return context

class Login(LoginView):
    # Staff: staff_1, Pass: 0339497769k
    # Admin: tiah_1, Pass: 11223344k
    form_class = forms.LoginForm
    template_name = 'login.html'

class Logout(LogoutView):
    template_name = 'logout.html'

class Register(CreateView):
    template_name = 'register.html'
    form_class = forms.RegisterForm

    def form_valid(self, form):
        user = form.save()  # formの情報を保存
        return redirect('register_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context

class RegisterSuccess(TemplateView):
    template_name = 'register_done.html'

class MyInfo(LoginRequiredMixin, TemplateView):
    User = get_user_model()
    model = User
    template_name = 'info/my_info.html'

class InfoUpdate(LoginRequiredMixin, UpdateView):
    User = get_user_model()
    model = User
    form_class = forms.UserUpdateForm
    template_name = 'info/info_update.html'

    def get_success_url(self):
        return resolve_url('my_info')

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.id)

class UserUpdateWorkinginfo(LoginRequiredMixin, UpdateView):
    User = get_user_model()
    model = User
    form_class = forms.WorkInfoUpdateForm
    template_name = 'info/workinginfo_update.html'

    def get_success_url(self):
        return resolve_url('my_info')

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "勤務情報修正"
        return context

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.id)

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = forms.PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'info/info_update.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context

class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'info/password_change_done.html'

#Honne
@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.HonneMiddleware, name='dispatch')
class HonneSheet(TemplateView):
    template_name = "honne/honne_sheet.html"
    form_class = forms.HonneForm

    def get_context_data(self, **kwargs):
        evaluation_unit = self.kwargs['evaluationUnit']
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        index_list = [0 for i in range(8)]
        initial_values = {
            "flg_finished": False,
        }
        evaluation_period = get_object_or_404(
            HonneEvaluationPeriod,
            pk=evaluation_unit,
            company_id=company_id,
            evaluation_start__lte=datetime.date.today(),
            evaluation_end__gte=datetime.date.today()
        )

        honne_questions = evaluation_period.honne_questions.prefetch_related(
            Prefetch(
                'honne_results',
                queryset=(
                    HonneAnswerResult.objects
                        .filter(evaluation_period_id=evaluation_unit,user_id=user_id,company_id=company_id)
                )
            )
        ).all().annotate(
            answer_value=HonneAnswerResult.objects.filter(
                honne_question=OuterRef("pk"),
                evaluation_period_id=evaluation_unit,
                company_id=company_id,
                user_id=user_id
            ).values('answer')[:1]
        ).filter((Q(apply_start_date__lte=datetime.date.today()) | Q(apply_start_date__isnull=True)) & ( Q(apply_end_date__isnull=True) | Q(apply_end_date__gte=datetime.date.today()))).filter().order_by('sort_no')
        honne_questions = honne_questions.filter(Q(apply_start_date__isnull=False) | Q(apply_end_date__isnull=False) )
        obj_index = evaluation_period.honne_index_results.filter(user_id=user_id,company_id=company_id).first()
        obj_type = evaluation_period.honne_type_results.filter(user_id=user_id,company_id=company_id).first()
        if obj_index is not None :
            index_list = [obj_index.kartet_index1, obj_index.kartet_index2, obj_index.kartet_index3, obj_index.kartet_index4, obj_index.kartet_index5, obj_index.kartet_index6, obj_index.kartet_index7, obj_index.kartet_index8]
        if obj_type is not None:
            initial_values['flg_finished'] = obj_type.flg_finished
        
        kwargs = super(HonneSheet, self).get_context_data(**kwargs)
        kwargs['questions'] = honne_questions
        kwargs['q_list'] = list(honne_questions.values_list('id', flat=True))
        kwargs['index_list'] = index_list
        kwargs['evaluation_unit'] = evaluation_unit
        kwargs['disabled'] = 'disabled' if initial_values['flg_finished'] else ''
        kwargs['form'] = self.form_class(initial_values)
        kwargs['title_header'] = "HONNE"

        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        # context['form'] = form
        if form.is_valid():
            key_evaluation_unit = self.kwargs['evaluationUnit']
            company_id = self.request.user.company_id
            user_id = self.request.user.id
            flg_finished = self.request.POST.get("flg_finished") or False
            honne_questions = HonneEvaluationPeriod.objects.filter(
                id=key_evaluation_unit,
                company_id=company_id
            ).first().honne_questions.all().order_by('sort_no')

            kartet_type_a = 0
            kartet_type_b = 0
            kartet_type_c = 0
            kartet_type_d = 0

            kartet_index_1 = 0
            kartet_index_2 = 0
            kartet_index_3 = 0
            kartet_index_4 = 0
            kartet_index_5 = 0
            kartet_index_6 = 0
            kartet_index_7 = 0
            kartet_index_8 = 0

            flag_update = False
            for q in honne_questions:
                strparam = 'kartet_answer_' + str(q.id)
                if len(self.request.POST.getlist(strparam)) == 0 or self.request.POST.getlist(strparam)[0] == '-':
                    continue
                answer = int(self.request.POST.getlist(strparam)[0])
                flag_update = True
                if q.group == 'A':
                    kartet_type_a = kartet_type_a + answer
                if q.group == 'B':
                    kartet_type_b = kartet_type_b + answer
                if q.group == 'C':
                    kartet_type_c = kartet_type_c + answer
                if q.group == 'D':
                    kartet_type_d = kartet_type_d + answer

                if q.acc1:
                    kartet_index_1 = kartet_index_1 + answer
                if q.acc2:
                    kartet_index_2 = kartet_index_2 + answer
                if q.acc3:
                    kartet_index_3 = kartet_index_3 + answer
                if q.acc4:
                    kartet_index_4 = kartet_index_4 + answer
                if q.acc5:
                    kartet_index_5 = kartet_index_5 + answer
                if q.acc6:
                    kartet_index_6 = kartet_index_6 + answer
                if q.acc7:
                    kartet_index_7 = kartet_index_7 + answer
                if q.acc8:
                    kartet_index_8 = kartet_index_8 + answer

                obj = HonneAnswerResult.objects.update_or_create(
                    company_id=company_id,
                    user_id=user_id,
                    evaluation_period_id=key_evaluation_unit,
                    honne_question_id=q.id,
                    defaults={
                        "answer": answer,
                        "answer_date": datetime.date.today(),
                    }
                )

            if flag_update == True:
                obj = HonneTypeResult.objects.update_or_create(
                    company_id=company_id,
                    user_id=user_id,
                    evaluation_period_id=key_evaluation_unit,
                    defaults={
                        "kartet_type_a": kartet_type_a,
                        "kartet_type_b": kartet_type_b,
                        "kartet_type_c": kartet_type_c,
                        "kartet_type_d": kartet_type_d,
                        "flg_finished": bool(flg_finished),
                    }
                )

                obj = HonneIndexResult.objects.update_or_create(
                    company_id=company_id,
                    user_id=user_id,
                    evaluation_period_id=key_evaluation_unit,
                    defaults={
                        "kartet_index1": kartet_index_1,
                        "kartet_index2": kartet_index_2,
                        "kartet_index3": kartet_index_3,
                        "kartet_index4": kartet_index_4,
                        "kartet_index5": kartet_index_5,
                        "kartet_index6": kartet_index_6,
                        "kartet_index7": kartet_index_7,
                        "kartet_index8": kartet_index_8,
                    }
                )
            else:
                obj = HonneTypeResult.objects.update_or_create(
                    company_id=company_id,
                    user_id=user_id,
                    evaluation_period_id=key_evaluation_unit,
                    defaults={
                        "flg_finished": bool(flg_finished),
                    }
                )

            context = self.get_context_data(**kwargs)
            context["message"] = '-- 保存しました。--'

        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.HonneTotalMiddleware, name='dispatch')
class HonneTotal(TemplateView):
    template_name = "honne/honne_total.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneTotal, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        list_result = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
        }
        kwargs['result'] = list_result
        kwargs['title_header'] = "HONNE"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        company_id = self.request.user.company_id
        context["form"] = form
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            evaluation_unit = HonneEvaluationPeriod.objects.all().filter(id=key_evaluation_unit,honne_type_results__company_id=company_id).annotate(
               total_a=Sum('honne_type_results__kartet_type_a'),
               total_b=Sum('honne_type_results__kartet_type_b'),
               total_c=Sum('honne_type_results__kartet_type_c'),
               total_d=Sum('honne_type_results__kartet_type_d'),
            ).first()
            if evaluation_unit is not None:
                list_type = ["A","B","C","D"]
                context['result']["A"] = evaluation_unit.total_a
                context['result']["B"] = evaluation_unit.total_b
                context['result']["C"] = evaluation_unit.total_c
                context['result']["D"] = evaluation_unit.total_d
                if sum(context['result'].values()) > 0:
                    context['max_type'] = max(context['result'], key=context['result'].get)
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.HonneTotalMiddleware, name='dispatch')
class HonneTypeStaticks(TemplateView):
    template_name = "honne/honne_type_staticks.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneTypeStaticks, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "HONNE"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            result_queryset = HonneTypeResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
            if key_user_id != '':
                result_queryset = result_queryset.filter(user_id=key_user_id)
            context['orderby_records'] = result_queryset
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.HonneTotalMiddleware, name='dispatch')
class HonneTypePersonalGraph(TemplateView):
    template_name = "honne/honne_type_personal_graph.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneTypePersonalGraph, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "HONNE"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            result_queryset = HonneTypeResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
            if key_user_id != '':
                result_queryset = result_queryset.filter(user_id=key_user_id)
            context['orderby_records'] = result_queryset
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.HonneTotalMiddleware, name='dispatch')
class HonneIndexStaticks(TemplateView):
    template_name = "honne/honne_index_staticks.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneIndexStaticks, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "HONNE"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            result_queryset = HonneIndexResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
            if key_user_id != '':
                result_queryset = result_queryset.filter(user_id=key_user_id)

            result_queryset = result_queryset.annotate(sum_kartet=F('kartet_index1') + F('kartet_index2') + F('kartet_index3') + F('kartet_index4') + F('kartet_index5') + F('kartet_index6') + F('kartet_index7') + F('kartet_index8'))
            context['orderby_records'] = result_queryset
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.HonneTotalMiddleware, name='dispatch')
class HonneChart(TemplateView):
    template_name = "honne/honne_chart.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneChart, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "HONNE"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            result_queryset = HonneIndexResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
            if key_user_id != '':
                result_queryset = result_queryset.filter(user_id=key_user_id)
            context['orderby_records'] = result_queryset
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.HonneTotalMiddleware, name='dispatch')
class HonneQrStaticks(TemplateView):
    template_name = "honne/honne_qr_staticks.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneQrStaticks, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "HONNE"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        context["qr_list"] = ""
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            question_list = HonneEvaluationPeriod.objects.filter(id=key_evaluation_unit).first().honne_questions.all()

            if len(question_list) > 0:
                result_queryset = HonneAnswerResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
                staff_list = User.objects.filter(company_id=request.user.company_id,id__in=result_queryset.values('user_id')).order_by('id')
                if key_user_id != '':
                    result_queryset = result_queryset.filter(user_id=key_user_id)
                    staff_list = staff_list.filter(id=key_user_id)
                context["staff_list"] = staff_list

                rowidx = 0
                result_list = [[[] for i in range(len(staff_list) + 1)] for j in range(len(question_list))]
                print(result_list)
                # pdb.set_trace()
                for mst in question_list:
                    result_list[rowidx][0] = mst.question
                    colidx = 1
                    for i in staff_list:
                        get_result = result_queryset.filter(honne_question_id=mst.id, user_id=i.id).first()
                        if get_result is None:
                            result_list[rowidx][colidx] = ''
                        else:
                            if get_result.answer == 1:
                                result_list[rowidx][colidx] = '○'
                            else:
                                result_list[rowidx][colidx] = '✕'
                        colidx = colidx + 1
                    rowidx = rowidx + 1
                context["qr_list"] = result_list
        return self.render_to_response(context)

# Selfcheck
@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.SelfcheckTotalMiddleware, name='dispatch')
class SelfcheckIndex(TemplateView):
    template_name = "selfcheck/selfcheck_index.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckIndex, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "SELFCHECK"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            result_queryset = SelfcheckIndexResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
            if key_user_id != '':
                result_queryset = result_queryset.filter(user_id=key_user_id)
            result_queryset = result_queryset.annotate(sum_selfcheck_index=F('selfcheck_index1') + F('selfcheck_index2') + F('selfcheck_index3') + F('selfcheck_index4') + F('selfcheck_index5') + F('selfcheck_index6') + F('selfcheck_index7') + F('selfcheck_index8') + F('selfcheck_index9') + F('selfcheck_index10') + F('selfcheck_index11') + F('selfcheck_index12'))
            context['orderby_records'] = result_queryset
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.SelfcheckTotalMiddleware, name='dispatch')
class SelfcheckIndexChart(TemplateView):
    template_name = "selfcheck/selfcheck_index_chart.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckIndexChart, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "SELFCHECK"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            result_queryset = SelfcheckIndexResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
            if key_user_id != '':
                result_queryset = result_queryset.filter(user_id=key_user_id)
            context['orderby_records'] = result_queryset
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.SelfcheckTotalMiddleware, name='dispatch')
class SelfcheckQuestions(TemplateView):
    template_name = "selfcheck/selfcheck_questions.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckQuestions, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "SELFCHECK"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        context["qr_list"] = ""
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            question_list = SelfcheckEvaluationPeriod.objects.filter(id=key_evaluation_unit).first().selfcheck_questions.all().order_by('category_id', 'sort_no')

            if len(question_list) > 0:
                result_queryset = SelfcheckAnswerResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
                staff_list = User.objects.filter(company_id=request.user.company_id,id__in=result_queryset.values('user_id')).order_by('id')
                if key_user_id != '':
                    result_queryset = result_queryset.filter(user_id=key_user_id)
                    staff_list = staff_list.filter(id=key_user_id)
                context["staff_list"] = staff_list
                # print(staff_list)
                # pdb.set_trace()

                rowidx = 0
                result_list = [[[] for i in range(len(staff_list) + 1)] for j in range(len(question_list))]

                for i in question_list:
                    colidx = 1
                    result_list[rowidx][0] = i.question
                    for staff in staff_list:
                        get_result = result_queryset.filter(selfcheck_question_id=i.id, user_id=staff.id).first()
                        result_list[rowidx][colidx] = '*'
                        if get_result is not None:
                            for element in SELFCHECK_ANSWER:
                                if int(element[0]) == get_result.selfcheck_answer:
                                    result_list[rowidx][colidx] = element[1]
                        colidx = colidx + 1
                    rowidx = rowidx + 1

                context["qr_list"] = result_list
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.SelfcheckTotalMiddleware, name='dispatch')
class SelfcheckType(TemplateView):
    template_name = "selfcheck/selfcheck_type.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckType, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "SELFCHECK"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            result_queryset = SelfcheckTypeResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
            if key_user_id != '':
                result_queryset = result_queryset.filter(user_id=key_user_id)
            context['orderby_records'] = result_queryset
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.SelfcheckTotalMiddleware, name='dispatch')
class SelfcheckTypeChart(TemplateView):
    template_name = "selfcheck/selfcheck_type_chart.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckTypeChart, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "SELFCHECK"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        if form.is_valid():
            key_evaluation_unit = request.POST['evaluation_unit']
            key_user_id = request.POST['user_id']
            result_queryset = SelfcheckTypeResult.objects.select_related('user').all().filter(evaluation_period_id=key_evaluation_unit)
            if key_user_id != '':
                result_queryset = result_queryset.filter(user_id=key_user_id)
            context['orderby_records'] = result_queryset
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.SelfcheckMiddleware, name='dispatch')
class SelfcheckSheet(TemplateView):
    template_name = 'selfcheck/selfcheck_sheet.html'
    form_class = forms.SelfcheckForm

    def get_context_data(self, **kwargs):
        evaluation_unit = self.kwargs['evaluationUnit']
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        index_list = [0 for i in range(12)]
        type_list = [0 for i in range(3)]
        questions = [{} for i in range(12)]
        initial_values = {
            "flg_finished": False,
        }
        questions[0] = {
            "label": '❶決断力',
            "q_list": []
        }
        questions[1] = {
            "label": '❷専門性',
            "q_list": []
        }
        questions[2] = {
            "label": '❸自己管理',
            "q_list": []
        }
        questions[3] = {
            "label": '❹広報力',
            "q_list": []
        }
        questions[4] = {
            "label": '❺連携力',
            "q_list": []
        }
        questions[5] = {
            "label": '❻人間関係',
            "q_list": []
        }
        questions[6] = {
            "label": '⑦対応力',
            "q_list": []
        }
        questions[7] = {
            "label": '⑧チームワーク力',
            "q_list": []
        }
        questions[8] = {
            "label": '⑨総合管理',
            "q_list": []
        }
        questions[9] = {
            "label": '⑩理念浸透',
            "q_list": []
        }
        questions[10] = {
            "label": '⑪自己啓発',
            "q_list": []
        }
        questions[11] = {
            "label": '⑫思考',
            "q_list": []
        }

        evaluation_period = get_object_or_404(
            SelfcheckEvaluationPeriod,
            pk=evaluation_unit,
            company_id=company_id,
            evaluation_start__lte=datetime.date.today(),
            evaluation_end__gte=datetime.date.today()
        )
        selfcheck_roles = []
        if self.request.user.role is not None:
            selfcheck_roles = Role.objects.filter(id=self.request.user.role.id).first().selfcheck_roles.all()

        selfcheck_questions = evaluation_period.selfcheck_questions.filter(selfcheck_roles__in=selfcheck_roles).prefetch_related(
            Prefetch(
                'selfcheck_results',
                queryset=(
                    SelfcheckAnswerResult.objects
                        .filter(evaluation_period_id=evaluation_unit,user_id=user_id,company_id=company_id)
                )
            )
        ).all().annotate(
            answer_value=SelfcheckAnswerResult.objects.filter(
                selfcheck_question=OuterRef("pk"),
                evaluation_period_id=evaluation_unit,
                company_id=company_id,
                user_id=user_id
            ).values('selfcheck_answer')[:1]
        ).order_by('sort_no').distinct()

        obj_index = evaluation_period.selfcheck_index_results.filter(user_id=user_id,company_id=company_id).first()
        obj_type = evaluation_period.selfcheck_type_results.filter(user_id=user_id,company_id=company_id).first()
        if obj_index is not None :
            index_list = [obj_index.selfcheck_index1, obj_index.selfcheck_index2, obj_index.selfcheck_index3, obj_index.selfcheck_index4, obj_index.selfcheck_index5, obj_index.selfcheck_index6, obj_index.selfcheck_index7, obj_index.selfcheck_index8, obj_index.selfcheck_index9, obj_index.selfcheck_index10, obj_index.selfcheck_index11, obj_index.selfcheck_index12]
        if obj_type is not None:
            initial_values['flg_finished'] = obj_type.flg_finished
            type_list[0] = obj_type.selfcheck_circl
            type_list[1] = obj_type.selfcheck_square
            type_list[2] = obj_type.selfcheck_traiangle

        for q in selfcheck_questions:
            questions[q.category_id-1]['q_list'].append(q)

        kwargs = super(SelfcheckSheet, self).get_context_data(**kwargs)
        kwargs['answer_choices'] = SELFCHECK_ANSWER
        kwargs['circl_list'] = CIRCL
        kwargs['square_list'] = SQUARE
        kwargs['traiangle_list'] = TRAIANGLE
        kwargs['questions'] = questions
        kwargs['q_list'] = list(selfcheck_questions.values_list('id', flat=True))
        kwargs['index_list'] = index_list
        kwargs['type_list'] = type_list
        kwargs['evaluation_unit'] = evaluation_unit
        kwargs['disabled'] = 'disabled' if initial_values['flg_finished'] else ''
        kwargs['form'] = self.form_class(initial_values)
        kwargs['title_header'] = "SELFCHECK"
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)

        if form.is_valid():
            key_evaluation_unit = self.kwargs['evaluationUnit']
            company_id = self.request.user.company_id
            user_id = self.request.user.id
            flg_finished = self.request.POST.get("flg_finished") or False
            selfcheck_questions = SelfcheckEvaluationPeriod.objects.filter(
                id=key_evaluation_unit,
                company_id=company_id
            ).first().selfcheck_questions.all().order_by('sort_no')

            selfcheck_type_circl = 0
            selfcheck_type_square = 0
            selfcheck_type_traiangle = 0

            selfcheck_index = [0 for i in range(12)]

            flag_update = False
            for q in selfcheck_questions:
                strparam = 'selfcheck_answer_' + str(q.id)
                if len(self.request.POST.getlist(strparam)) == 0 or self.request.POST.getlist(strparam)[0] == '':
                    continue
                answer = int(self.request.POST.getlist(strparam)[0])
                flag_update = True
                selfcheck_index[q.category_id - 1] = selfcheck_index[q.category_id - 1] + answer
                if q.category_id in CIRCL:
                    selfcheck_type_circl = selfcheck_type_circl + answer
                if q.category_id in SQUARE:
                    selfcheck_type_square = selfcheck_type_square + answer
                if q.category_id in TRAIANGLE:
                    selfcheck_type_traiangle = selfcheck_type_traiangle + answer

                obj = SelfcheckAnswerResult.objects.update_or_create(
                    company_id=company_id,
                    user_id=user_id,
                    evaluation_period_id=key_evaluation_unit,
                    selfcheck_question_id=q.id,
                    defaults={
                        "selfcheck_answer": answer,
                        "selfcheck_answer_date": datetime.date.today(),
                    }
                )

            if flag_update == True:
                obj = SelfcheckTypeResult.objects.update_or_create(
                    company_id=company_id,
                    user_id=user_id,
                    evaluation_period_id=key_evaluation_unit,
                    defaults={
                        "selfcheck_circl": selfcheck_type_circl,
                        "selfcheck_square": selfcheck_type_square,
                        "selfcheck_traiangle": selfcheck_type_traiangle,
                        "flg_finished": bool(flg_finished),
                    }
                )

                obj = SelfcheckIndexResult.objects.update_or_create(
                    company_id=company_id,
                    user_id=user_id,
                    evaluation_period_id=key_evaluation_unit,
                    defaults={
                        "selfcheck_index1": selfcheck_index[0],
                        "selfcheck_index2": selfcheck_index[1],
                        "selfcheck_index3": selfcheck_index[2],
                        "selfcheck_index4": selfcheck_index[3],
                        "selfcheck_index5": selfcheck_index[4],
                        "selfcheck_index6": selfcheck_index[5],
                        "selfcheck_index7": selfcheck_index[6],
                        "selfcheck_index8": selfcheck_index[7],
                        "selfcheck_index9": selfcheck_index[8],
                        "selfcheck_index10": selfcheck_index[9],
                        "selfcheck_index11": selfcheck_index[10],
                        "selfcheck_index12": selfcheck_index[11],
                    }
                )
            else:
                obj = SelfcheckTypeResult.objects.update_or_create(
                    company_id=company_id,
                    user_id=user_id,
                    evaluation_period_id=key_evaluation_unit,
                    defaults={
                        "flg_finished": bool(flg_finished),
                    }
                )

            context = self.get_context_data(**kwargs)
            context["message"] = '-- 保存しました。--'

        return self.render_to_response(context)

#Bonknow
@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.BonknowMiddleware, name='dispatch')
class BonknowSheet(TemplateView):
    template_name = "bonknow/bonknow_sheet.html"
    form_class = forms.BonknowSheetForm

    def get_context_data(self, **kwargs):
        key_evaluation_unit = self.kwargs['evaluationUnit']
        evaluation_unit = self.kwargs['evaluationUnit']
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        initial_values = {
            'flg_finished': False
        }

        evaluation_period = get_object_or_404(
            BonknowEvaluationPeriod,
            pk=evaluation_unit,
            company_id=company_id,
            evaluation_start__lte=datetime.date.today(),
            evaluation_end__gte=datetime.date.today()
        )

        respons_questions = evaluation_period.respons_questions.prefetch_related(
            Prefetch(
                'respons_answers',
                queryset=(
                    ResponsAnswer.objects
                        .filter(evaluation_period_id=evaluation_unit,user_id=user_id,company_id=company_id)
                )
            )
        ).all().annotate(
            answer_value=ResponsAnswer.objects.filter(
                respons_question=OuterRef("pk"),
                evaluation_period_id=evaluation_unit,
                company_id=company_id,
                user_id=user_id
            ).values('answer')[:1]
        ).filter((Q(apply_start_date__lte=datetime.date.today()) | Q(apply_start_date__isnull=True)) & ( Q(apply_end_date__isnull=True) | Q(apply_end_date__gte=datetime.date.today()))).order_by('sort_no')

        obj = ResponsResult.objects.filter(
            company_id=company_id,
            user_id=user_id,
            evaluation_period_id=key_evaluation_unit
        ).first()

        if obj is not None:
            initial_values['flg_finished'] = obj.flg_finished

        think_questions = evaluation_period.think_questions.prefetch_related(
            Prefetch(
                'think_answers',
                queryset=(
                    ThinkAnswer.objects
                        .filter(evaluation_period_id=evaluation_unit,user_id=user_id,company_id=company_id)
                )
            )
        ).all().annotate(
            answer_value=ThinkAnswer.objects.filter(
                think_question=OuterRef("pk"),
                evaluation_period_id=evaluation_unit,
                company_id=company_id,
                user_id=user_id
            ).values('answer')[:1]
        ).filter((Q(apply_start_date__lte=datetime.date.today()) | Q(apply_start_date__isnull=True)) & ( Q(apply_end_date__isnull=True) | Q(apply_end_date__gte=datetime.date.today()))).order_by('sort_no')

        kwargs = super(BonknowSheet, self).get_context_data(**kwargs)
        kwargs['evaluation_unit'] = evaluation_unit
        kwargs['respons_questions'] = respons_questions
        kwargs['think_questions'] = think_questions
        kwargs['think_list'] = list(think_questions.values_list('id', flat=True))
        kwargs['res_list'] = list(respons_questions.values_list('id', flat=True))
        kwargs['form'] = self.form_class(initial_values)
        kwargs['disabled'] = 'disabled' if initial_values['flg_finished'] else ''
        kwargs['title_header'] = "BONKNOW"
        return kwargs

    def post(self, request, *args, **kwargs):
        key_evaluation_unit = self.kwargs['evaluationUnit']
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        evaluation_unit = BonknowEvaluationPeriod.objects.filter(
            id=key_evaluation_unit,
            company_id=company_id
        ).first()
        respons_questions = evaluation_unit.respons_questions.all().order_by('sort_no')
        think_questions = evaluation_unit.think_questions.all().order_by('sort_no')
        sense = self.request.POST.getlist('sense')[0]
        logic = self.request.POST.getlist('logic')[0]
        for rq in respons_questions:
            strparam = 'respons_answer_' + str(rq.id)
            if len(self.request.POST.getlist(strparam)) == 0 or self.request.POST.getlist(strparam)[0] == '':
                continue
            answer = int(self.request.POST.getlist(strparam)[0])
            # if (rq.question_type == '1' and answer == 1) or (rq.question_type == '2' and answer == 0):
            #     logic += 1
            # if (rq.question_type == '2' and answer == 1) or (rq.question_type == '1' and answer == 0):
            #     sense += 1
            obj = ResponsAnswer.objects.update_or_create(
                company_id=company_id,
                user_id=user_id,
                evaluation_period_id=key_evaluation_unit,
                respons_question_id=rq.id,
                defaults={
                    "answer": answer,
                    "answer_date": datetime.date.today(),
                }
            )

        flg_finished = self.request.POST.get('flg_finished') or False
        if flg_finished:
            flg_finished  = True
       
        obj = ResponsResult.objects.update_or_create(
            company_id=company_id,
            user_id=user_id,
            evaluation_period_id=key_evaluation_unit,
            defaults={
                "logic": logic,
                "sense": sense,
                "review_date": datetime.date.today(),
                'flg_finished': flg_finished
            }
        )

        must = self.request.POST.getlist('must')[0]
        want = self.request.POST.getlist('want')[0]
        for tq in think_questions:
            strparam = 'think_answer_' + str(tq.id)
            if len(self.request.POST.getlist(strparam)) == 0 or self.request.POST.getlist(strparam)[0] == '':
                continue
            answer = int(self.request.POST.getlist(strparam)[0])
            # if (rq.question_type == '1' and answer == 1) or (rq.question_type == '2' and answer == 0):
            #     must += 1
            # if (rq.question_type == '2' and answer == 1) or (rq.question_type == '1' and answer == 0):
            #     want += 1

            obj = ThinkAnswer.objects.update_or_create(
                company_id=company_id,
                user_id=user_id,
                evaluation_period_id=key_evaluation_unit,
                think_question_id=tq.id,
                defaults={
                    "answer": answer,
                    "answer_date": datetime.date.today(),
                }
            )

        obj = ThinkResult.objects.update_or_create(
            company_id=company_id,
            user_id=user_id,
            evaluation_period_id=key_evaluation_unit,
            defaults={
                "must": must,
                "want": want,
                "review_date": datetime.date.today()
            }
        )

        context = self.get_context_data(**kwargs)
        context["message"] = '-- 保存しました。--'

        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.BonknowTotalMiddleware, name='dispatch')
class BonknowRespons(TemplateView):
    template_name = "bonknow/bonknow_respons.html"
    form_class = forms.BonknowForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id

        kwargs = super(BonknowRespons, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request.GET or None)
        kwargs['title_header'] = 'BONKNOW'
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        context["form"] = form
        key_evaluation_unit = request.POST['evaluation_unit']
        results = ResponsResult.objects.all().filter(id=key_evaluation_unit,user_id=request.user.id).order_by('review_date')
        context['times'] = [];
        context['logic'] = [];
        context['sense'] = [];
        for result in results:
            context['times'].append(result.evaluation_period.evaluation_name)
            context['logic'].append(result.logic)
            context['sense'].append(result.sense)

        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.BonknowTotalMiddleware, name='dispatch')
class BonknowThink(TemplateView):
    template_name = "bonknow/bonknow_think.html"
    form_class = forms.BonknowForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id

        kwargs = super(BonknowThink, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request.GET or None)
        kwargs['title_header'] = 'BONKNOW'
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        context["form"] = form
        key_evaluation_unit = request.POST['evaluation_unit']
        results = ThinkResult.objects.all().filter(id=key_evaluation_unit,user_id=request.user.id).order_by('review_date')
        context['times'] = [];
        context['must'] = [];
        context['want'] = [];
        for result in results:
            # str_time = result.review_date.strftime('%Y/%m')
            context['times'].append(result.evaluation_period.evaluation_name)
            context['must'].append(result.must)
            context['want'].append(result.want)

        return self.render_to_response(context)

#MASMASMANDARA
@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.MandaraMiddleware, name='dispatch')
class MandaraCreate(TemplateView):
    template_name = "mandara/mandara_create.html"
    form_class = forms.MandaraCreateForm

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        mandara = MandaraBase.objects.all().filter(
            Q(user_id=user_id) & Q(company_id=company_id) & (Q(mandara_period__start_date__gt=today) | Q(flg_finished=False))
        ).order_by('mandara_period__start_date').first()
        kwargs['form'] = self.form_class(initial={'field_stop': 'total_mission'})
        mandara_periods = MandaraPeriod.objects.all().filter(Q(company_id=company_id) & Q(start_date__gt=today)
        ).order_by('start_date')
        kwargs['form'] = self.form_class(initial={'field_stop': 'total_mission'})
        if mandara is not None:
            kwargs['form'] = self.form_class(instance=mandara)
        kwargs['mandara'] = mandara
        kwargs['mandara_periods'] = mandara_periods
        kwargs['title_header'] = "MASMASMANDARA"
        print(mandara)
        return kwargs

    def post(self, request, *args, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST, instance=context["mandara"])
        context["form"] = form
        context["message_class"] = 'text-danger'
        start_YYYYMM = request.POST.get('start_YYYYMM')
        end_YYYYMM = request.POST.get('end_YYYYMM')

        if form.is_valid():
            mandara_period = None
            if start_YYYYMM:
                mandara_period = MandaraPeriod.objects.filter(id=start_YYYYMM,company_id=company_id).first()
            
            mandara = form.save(commit=False)
            mandara.user_id = user_id
            mandara.company_id = company_id
            mandara.mandara_period = mandara_period
            if 'save' in request.POST:
                mandara.flg_finished = True
                if context["mandara"] is not None:
                    MandaraProgress.objects.filter(mandara_base_id=context["mandara"].id).delete()
                if mandara_period is not None:
                    sdate = mandara_period.start_date   # start date
                    edate = mandara_period.end_date   # end date
                    delta = edate - sdate
                    bulk_list = list()
                    for i in range(delta.days + 1):
                        day = sdate + datetime.timedelta(days=i)
                        bulk_list.append(
                            MandaraProgress(date=day, mandara_base_id=mandara.id)
                        )

                    bulk_msj = MandaraProgress.objects.bulk_create(bulk_list)
            mandara.save()
            context['mandara'] = mandara
            context["message"] = '-- 保存しました。--'
            context["message_class"] = 'text-success'
        else:
            context["message"] = form.errors.as_data()

        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.MandaraMiddleware, name='dispatch')    
class MandaraSheet(TemplateView):
    template_name = "mandara/mandara_sheet.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["title_header"] = "MANDARA" 
        return kwargs
    
@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.MandaraMiddleware, name='dispatch')    
class MandaraReuse(TemplateView):
    template_name = "mandara/mandara_reuse.html"

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        today = datetime.date.today()
        mandara = MandaraBase.objects.select_related('mandara_period').filter(user_id=user_id,company_id=company_id,mandara_period__end_date__gte=today,mandara_period__start_date__lte=today,flg_finished=True).annotate(
               A1_result=Coalesce(Sum('mandara_progress__A1_result'), 0),
               A2_result=Coalesce(Sum('mandara_progress__A2_result'), 0),
               A3_result=Coalesce(Sum('mandara_progress__A3_result'), 0),
               A4_result=Coalesce(Sum('mandara_progress__A4_result'), 0),
               A5_result=Coalesce(Sum('mandara_progress__A5_result'), 0),
               A6_result=Coalesce(Sum('mandara_progress__A6_result'), 0),
               A7_result=Coalesce(Sum('mandara_progress__A7_result'), 0),
               A8_result=Coalesce(Sum('mandara_progress__A8_result'), 0),
               B1_result=Coalesce(Sum('mandara_progress__B1_result'), 0),
               B2_result=Coalesce(Sum('mandara_progress__B2_result'), 0),
               B3_result=Coalesce(Sum('mandara_progress__B3_result'), 0),
               B4_result=Coalesce(Sum('mandara_progress__B4_result'), 0),
               B5_result=Coalesce(Sum('mandara_progress__B5_result'), 0),
               B6_result=Coalesce(Sum('mandara_progress__B6_result'), 0),
               B7_result=Coalesce(Sum('mandara_progress__B7_result'), 0),
               B8_result=Coalesce(Sum('mandara_progress__B8_result'), 0),
               C1_result=Coalesce(Sum('mandara_progress__C1_result'), 0),
               C2_result=Coalesce(Sum('mandara_progress__C2_result'), 0),
               C3_result=Coalesce(Sum('mandara_progress__C3_result'), 0),
               C4_result=Coalesce(Sum('mandara_progress__C4_result'), 0),
               C5_result=Coalesce(Sum('mandara_progress__C5_result'), 0),
               C6_result=Coalesce(Sum('mandara_progress__C6_result'), 0),
               C7_result=Coalesce(Sum('mandara_progress__C7_result'), 0),
               C8_result=Coalesce(Sum('mandara_progress__C8_result'), 0),
               D1_result=Coalesce(Sum('mandara_progress__D1_result'), 0),
               D2_result=Coalesce(Sum('mandara_progress__D2_result'), 0),
               D3_result=Coalesce(Sum('mandara_progress__D3_result'), 0),
               D4_result=Coalesce(Sum('mandara_progress__D4_result'), 0),
               D5_result=Coalesce(Sum('mandara_progress__D5_result'), 0),
               D6_result=Coalesce(Sum('mandara_progress__D6_result'), 0),
               D7_result=Coalesce(Sum('mandara_progress__D7_result'), 0),
               D8_result=Coalesce(Sum('mandara_progress__D8_result'), 0),
               E1_result=Coalesce(Sum('mandara_progress__E1_result'), 0),
               E2_result=Coalesce(Sum('mandara_progress__E2_result'), 0),
               E3_result=Coalesce(Sum('mandara_progress__E3_result'), 0),
               E4_result=Coalesce(Sum('mandara_progress__E4_result'), 0),
               E5_result=Coalesce(Sum('mandara_progress__E5_result'), 0),
               E6_result=Coalesce(Sum('mandara_progress__E6_result'), 0),
               E7_result=Coalesce(Sum('mandara_progress__E7_result'), 0),
               E8_result=Coalesce(Sum('mandara_progress__E8_result'), 0),
               F1_result=Coalesce(Sum('mandara_progress__F1_result'), 0),
               F2_result=Coalesce(Sum('mandara_progress__F2_result'), 0),
               F3_result=Coalesce(Sum('mandara_progress__F3_result'), 0),
               F4_result=Coalesce(Sum('mandara_progress__F4_result'), 0),
               F5_result=Coalesce(Sum('mandara_progress__F5_result'), 0),
               F6_result=Coalesce(Sum('mandara_progress__F6_result'), 0),
               F7_result=Coalesce(Sum('mandara_progress__F7_result'), 0),
               F8_result=Coalesce(Sum('mandara_progress__F8_result'), 0),
               G1_result=Coalesce(Sum('mandara_progress__G1_result'), 0),
               G2_result=Coalesce(Sum('mandara_progress__G2_result'), 0),
               G3_result=Coalesce(Sum('mandara_progress__G3_result'), 0),
               G4_result=Coalesce(Sum('mandara_progress__G4_result'), 0),
               G5_result=Coalesce(Sum('mandara_progress__G5_result'), 0),
               G6_result=Coalesce(Sum('mandara_progress__G6_result'), 0),
               G7_result=Coalesce(Sum('mandara_progress__G7_result'), 0),
               G8_result=Coalesce(Sum('mandara_progress__G8_result'), 0),
               H1_result=Coalesce(Sum('mandara_progress__H1_result'), 0),
               H2_result=Coalesce(Sum('mandara_progress__H2_result'), 0),
               H3_result=Coalesce(Sum('mandara_progress__H3_result'), 0),
               H4_result=Coalesce(Sum('mandara_progress__H4_result'), 0),
               H5_result=Coalesce(Sum('mandara_progress__H5_result'), 0),
               H6_result=Coalesce(Sum('mandara_progress__H6_result'), 0),
               H7_result=Coalesce(Sum('mandara_progress__H7_result'), 0),
               H8_result=Coalesce(Sum('mandara_progress__H8_result'), 0),
            ).first()
        kwargs['mandara'] = mandara
        kwargs['month'] = datetime.date.today().strftime("%m")
        if mandara is not None:
            results = MandaraProgress.objects.all().filter(mandara_base_id=mandara.id,date__lte=datetime.date.today()).annotate(
                month=ExtractMonth('date'),
                year=ExtractYear('date')
            )
            kwargs['check_today'] = results.filter(date=datetime.date.today()).first()
            data = {}
            for i in results:
                key = str(i.year) + '/' + str(i.month)
                if key not in data:
                    data[key] = i.sum_result()
                else:
                    data[key] += i.sum_result()
            list_month = []
            list_value = []
            for key, value in data.items():
                list_month.append(key)
                list_value.append(value)

            kwargs['data_month'] = list_month
            kwargs['data_value'] = list_value
            
            kwargs['fix'] = True
            if mandara.mandara_period.start_date > today:
                kwargs['fix'] = False

            kwargs['start'] = mandara.mandara_period.display_time_start
            kwargs['end'] = mandara.mandara_period.display_time_end

        kwargs['title_header'] = "MASMASMANDARA"

        return kwargs

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.MandaraMiddleware, name='dispatch')
class MandaraCompletion(TemplateView):
    template_name = "mandara/mandara_completion.html"
    form_class = forms.MandaraCompleteForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        today_str = datetime.date.today()
        mandara_get = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,mandara_period__end_date__lt=today_str,flg_finished=True).order_by('mandara_period__start_date')
        mandara_periods = MandaraPeriod.objects.all().filter(Q(company_id=company_id) & Q(end_date__lt=today_str)).order_by('start_date')

        kwargs['mandara_get'] = mandara_get
        kwargs['mandara_get'] = mandara_get
        kwargs['form'] = self.form_class(company_id)
        kwargs['title_header'] = "MASMASMANDARA"
        return kwargs
    
    def post(self, request, *args, **kwargs):
        company_id = request.user.company_id
        context = self.get_context_data(**kwargs)
        form = self.form_class(company_id, request.POST)
        context["form"] = form
        start_YYYYMM = request.POST.get('start')
        end_YYYYMM = request.POST.get('end')
        
        if end_YYYYMM:
            context['mandara_get'] = context['mandara_get'].filter(mandara_period__end_date__lte=end_YYYYMM)
        if start_YYYYMM:
            context['mandara_get'] = context['mandara_get'].filter(mandara_period__start_date__gte=start_YYYYMM)
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.MandaraMiddleware, name='dispatch')    
class MandaraCompletionDetail(TemplateView):
    template_name = "mandara/mandara_completion_detail.html"

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        id = self.kwargs.get('id')
        get_mandara_detail = MandaraBase.objects.select_related('mandara_period').filter(user_id=user_id,company_id=company_id,id=id,flg_finished=True).annotate(
               A1_result=Coalesce(Sum('mandara_progress__A1_result'), 0),
               A2_result=Coalesce(Sum('mandara_progress__A2_result'), 0),
               A3_result=Coalesce(Sum('mandara_progress__A3_result'), 0),
               A4_result=Coalesce(Sum('mandara_progress__A4_result'), 0),
               A5_result=Coalesce(Sum('mandara_progress__A5_result'), 0),
               A6_result=Coalesce(Sum('mandara_progress__A6_result'), 0),
               A7_result=Coalesce(Sum('mandara_progress__A7_result'), 0),
               A8_result=Coalesce(Sum('mandara_progress__A8_result'), 0),
               B1_result=Coalesce(Sum('mandara_progress__B1_result'), 0),
               B2_result=Coalesce(Sum('mandara_progress__B2_result'), 0),
               B3_result=Coalesce(Sum('mandara_progress__B3_result'), 0),
               B4_result=Coalesce(Sum('mandara_progress__B4_result'), 0),
               B5_result=Coalesce(Sum('mandara_progress__B5_result'), 0),
               B6_result=Coalesce(Sum('mandara_progress__B6_result'), 0),
               B7_result=Coalesce(Sum('mandara_progress__B7_result'), 0),
               B8_result=Coalesce(Sum('mandara_progress__B8_result'), 0),
               C1_result=Coalesce(Sum('mandara_progress__C1_result'), 0),
               C2_result=Coalesce(Sum('mandara_progress__C2_result'), 0),
               C3_result=Coalesce(Sum('mandara_progress__C3_result'), 0),
               C4_result=Coalesce(Sum('mandara_progress__C4_result'), 0),
               C5_result=Coalesce(Sum('mandara_progress__C5_result'), 0),
               C6_result=Coalesce(Sum('mandara_progress__C6_result'), 0),
               C7_result=Coalesce(Sum('mandara_progress__C7_result'), 0),
               C8_result=Coalesce(Sum('mandara_progress__C8_result'), 0),
               D1_result=Coalesce(Sum('mandara_progress__D1_result'), 0),
               D2_result=Coalesce(Sum('mandara_progress__D2_result'), 0),
               D3_result=Coalesce(Sum('mandara_progress__D3_result'), 0),
               D4_result=Coalesce(Sum('mandara_progress__D4_result'), 0),
               D5_result=Coalesce(Sum('mandara_progress__D5_result'), 0),
               D6_result=Coalesce(Sum('mandara_progress__D6_result'), 0),
               D7_result=Coalesce(Sum('mandara_progress__D7_result'), 0),
               D8_result=Coalesce(Sum('mandara_progress__D8_result'), 0),
               E1_result=Coalesce(Sum('mandara_progress__E1_result'), 0),
               E2_result=Coalesce(Sum('mandara_progress__E2_result'), 0),
               E3_result=Coalesce(Sum('mandara_progress__E3_result'), 0),
               E4_result=Coalesce(Sum('mandara_progress__E4_result'), 0),
               E5_result=Coalesce(Sum('mandara_progress__E5_result'), 0),
               E6_result=Coalesce(Sum('mandara_progress__E6_result'), 0),
               E7_result=Coalesce(Sum('mandara_progress__E7_result'), 0),
               E8_result=Coalesce(Sum('mandara_progress__E8_result'), 0),
               F1_result=Coalesce(Sum('mandara_progress__F1_result'), 0),
               F2_result=Coalesce(Sum('mandara_progress__F2_result'), 0),
               F3_result=Coalesce(Sum('mandara_progress__F3_result'), 0),
               F4_result=Coalesce(Sum('mandara_progress__F4_result'), 0),
               F5_result=Coalesce(Sum('mandara_progress__F5_result'), 0),
               F6_result=Coalesce(Sum('mandara_progress__F6_result'), 0),
               F7_result=Coalesce(Sum('mandara_progress__F7_result'), 0),
               F8_result=Coalesce(Sum('mandara_progress__F8_result'), 0),
               G1_result=Coalesce(Sum('mandara_progress__G1_result'), 0),
               G2_result=Coalesce(Sum('mandara_progress__G2_result'), 0),
               G3_result=Coalesce(Sum('mandara_progress__G3_result'), 0),
               G4_result=Coalesce(Sum('mandara_progress__G4_result'), 0),
               G5_result=Coalesce(Sum('mandara_progress__G5_result'), 0),
               G6_result=Coalesce(Sum('mandara_progress__G6_result'), 0),
               G7_result=Coalesce(Sum('mandara_progress__G7_result'), 0),
               G8_result=Coalesce(Sum('mandara_progress__G8_result'), 0),
               H1_result=Coalesce(Sum('mandara_progress__H1_result'), 0),
               H2_result=Coalesce(Sum('mandara_progress__H2_result'), 0),
               H3_result=Coalesce(Sum('mandara_progress__H3_result'), 0),
               H4_result=Coalesce(Sum('mandara_progress__H4_result'), 0),
               H5_result=Coalesce(Sum('mandara_progress__H5_result'), 0),
               H6_result=Coalesce(Sum('mandara_progress__H6_result'), 0),
               H7_result=Coalesce(Sum('mandara_progress__H7_result'), 0),
               H8_result=Coalesce(Sum('mandara_progress__H8_result'), 0),
            ).first()
        
        # end_YYYYMM = get_mandara_detail.mandara_period.end_date
        # start_YYYYMM = get_mandara_detail.mandara_period.start_date

        # format_end_date = f'{end_YYYYMM.year} 年 {int(end_YYYYMM[4:])} 月'
        # format_start_date = f'{start_YYYYMM[:4]} 年 {int(start_YYYYMM[4:])} 月'

        month = datetime.date.today().strftime("%m")

        kwargs['get_mandara_detail'] = get_mandara_detail
        kwargs['format_end_date'] = get_mandara_detail.mandara_period.display_time_end
        kwargs['format_start_date'] = get_mandara_detail.mandara_period.display_time_start
        kwargs['month'] = month
        kwargs['title_header'] = "MASMASMANDARA"
        
        return kwargs

@login_required
def get_detail_month(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            try:
                company_id = request.user.company_id
                user_id = request.user.id
                today_str = datetime.date.today()
                year = datetime.date.today().strftime("%Y")
                month = datetime.date.today().strftime("%m")
                box = request.GET['type_box']
                mandara_get = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,mandara_period__end_date__gt=today_str).order_by('mandara_period__start_date').first()
                if mandara_get is not None:
                    list_resp = list(mandara_get.mandara_progress.annotate(day=ExtractDay('date')).filter(date__year=year,date__month=month).values('day', box + '_result'))
                    return JsonResponse({'context': list_resp})
            except:
                HttpResponseBadRequest('Invalid request')
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

@login_required
def post_detail_day(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            try:
                company_id = request.user.company_id
                user_id = request.user.id
                today_str = datetime.date.today()
                data = json.load(request)
                todo = data.get('box')
                field = todo + '_result'
                mandara_get = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,mandara_period__end_date__gt=today_str).order_by('mandara_period__start_date').first()
                if mandara_get is not None:
                    today_progress = MandaraProgress.objects.filter(mandara_base_id=mandara_get.id,date=datetime.date.today())
                    if not today_progress:
                        MandaraProgress.objects.create(mandara_base_id=mandara_get.id, date=datetime.date.today())
                        today_progress = today_progress
                    check = today_progress.values(todo+'_result').first()
                    if check[field] == 0:
                        today_progress.update(**{field: 1})
                        if 'A' in todo:
                            mandara_get.A_result += 1
                        if 'B' in todo:
                            mandara_get.B_result += 1 
                        if 'C' in todo:
                            mandara_get.C_result += 1 
                        if 'D' in todo:
                            mandara_get.D_result += 1 
                        if 'E' in todo:
                            mandara_get.E_result += 1 
                        if 'F' in todo:
                            mandara_get.F_result += 1 
                        if 'G' in todo:
                            mandara_get.G_result += 1 
                        if 'H' in todo:
                            mandara_get.H_result += 1
                        mandara_get.save()
                        return JsonResponse({'status': 'OK'})
            except:
                HttpResponseBadRequest('Invalid request')
        return JsonResponse({'status': 'NG'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

@login_required
def mandara_pdf(request, id):
    options = {
        'page-size': 'A4',
        'page-height': "10in",
        'page-width': "13in",
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'no-outline': None,
        'javascript-delay': 100,
    }

    template_path = 'mandara/mandara_print.html'
    template = get_template(template_path)
    company_id = request.user.company_id
    user_id = request.user.id
    mandara = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,id=id).annotate(
           A1_result=Sum('mandara_progress__A1_result'),
           A2_result=Sum('mandara_progress__A2_result'),
           A3_result=Sum('mandara_progress__A3_result'),
           A4_result=Sum('mandara_progress__A4_result'),
           A5_result=Sum('mandara_progress__A5_result'),
           A6_result=Sum('mandara_progress__A6_result'),
           A7_result=Sum('mandara_progress__A7_result'),
           A8_result=Sum('mandara_progress__A8_result'),
           B1_result=Sum('mandara_progress__B1_result'),
           B2_result=Sum('mandara_progress__B2_result'),
           B3_result=Sum('mandara_progress__B3_result'),
           B4_result=Sum('mandara_progress__B4_result'),
           B5_result=Sum('mandara_progress__B5_result'),
           B6_result=Sum('mandara_progress__B6_result'),
           B7_result=Sum('mandara_progress__B7_result'),
           B8_result=Sum('mandara_progress__B8_result'),
           C1_result=Sum('mandara_progress__C1_result'),
           C2_result=Sum('mandara_progress__C2_result'),
           C3_result=Sum('mandara_progress__C3_result'),
           C4_result=Sum('mandara_progress__C4_result'),
           C5_result=Sum('mandara_progress__C5_result'),
           C6_result=Sum('mandara_progress__C6_result'),
           C7_result=Sum('mandara_progress__C7_result'),
           C8_result=Sum('mandara_progress__C8_result'),
           D1_result=Sum('mandara_progress__D1_result'),
           D2_result=Sum('mandara_progress__D2_result'),
           D3_result=Sum('mandara_progress__D3_result'),
           D4_result=Sum('mandara_progress__D4_result'),
           D5_result=Sum('mandara_progress__D5_result'),
           D6_result=Sum('mandara_progress__D6_result'),
           D7_result=Sum('mandara_progress__D7_result'),
           D8_result=Sum('mandara_progress__D8_result'),
           E1_result=Sum('mandara_progress__E1_result'),
           E2_result=Sum('mandara_progress__E2_result'),
           E3_result=Sum('mandara_progress__E3_result'),
           E4_result=Sum('mandara_progress__E4_result'),
           E5_result=Sum('mandara_progress__E5_result'),
           E6_result=Sum('mandara_progress__E6_result'),
           E7_result=Sum('mandara_progress__E7_result'),
           E8_result=Sum('mandara_progress__E8_result'),
           F1_result=Sum('mandara_progress__F1_result'),
           F2_result=Sum('mandara_progress__F2_result'),
           F3_result=Sum('mandara_progress__F3_result'),
           F4_result=Sum('mandara_progress__F4_result'),
           F5_result=Sum('mandara_progress__F5_result'),
           F6_result=Sum('mandara_progress__F6_result'),
           F7_result=Sum('mandara_progress__F7_result'),
           F8_result=Sum('mandara_progress__F8_result'),
           G1_result=Sum('mandara_progress__G1_result'),
           G2_result=Sum('mandara_progress__G2_result'),
           G3_result=Sum('mandara_progress__G3_result'),
           G4_result=Sum('mandara_progress__G4_result'),
           G5_result=Sum('mandara_progress__G5_result'),
           G6_result=Sum('mandara_progress__G6_result'),
           G7_result=Sum('mandara_progress__G7_result'),
           G8_result=Sum('mandara_progress__G8_result'),
           H1_result=Sum('mandara_progress__H1_result'),
           H2_result=Sum('mandara_progress__H2_result'),
           H3_result=Sum('mandara_progress__H3_result'),
           H4_result=Sum('mandara_progress__H4_result'),
           H5_result=Sum('mandara_progress__H5_result'),
           H6_result=Sum('mandara_progress__H6_result'),
           H7_result=Sum('mandara_progress__H7_result'),
           H8_result=Sum('mandara_progress__H8_result'),
        ).first()
    context = {'mandara': mandara, 'request': request}
    html = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf=wkhtml_to_pdf)

    pdf = pdfkit.from_string(html, False,configuration=config, options=options)

    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename="wkhtml_to_pdf.pdf"'
    # print(response.status_code)
    if response.status_code != 200:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.MandaraTotalMiddleware, name='dispatch')
class MandaraPersonal(TemplateView):
    template_name = "mandara/mandara_personal.html"
    form_class = forms.MandaraForm

    def get_context_data(self, **kwargs):
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "MASMASMANDARA"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        company_id = self.request.user.company_id
        user_id = self.request.POST.get("user_id")

        today = datetime.date.today()
        mandara = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,mandara_period__end_date__gte=today,mandara_period__start_date__lte=today,flg_finished=True).annotate(
               A1_result=Sum('mandara_progress__A1_result'),
               A2_result=Sum('mandara_progress__A2_result'),
               A3_result=Sum('mandara_progress__A3_result'),
               A4_result=Sum('mandara_progress__A4_result'),
               A5_result=Sum('mandara_progress__A5_result'),
               A6_result=Sum('mandara_progress__A6_result'),
               A7_result=Sum('mandara_progress__A7_result'),
               A8_result=Sum('mandara_progress__A8_result'),
               B1_result=Sum('mandara_progress__B1_result'),
               B2_result=Sum('mandara_progress__B2_result'),
               B3_result=Sum('mandara_progress__B3_result'),
               B4_result=Sum('mandara_progress__B4_result'),
               B5_result=Sum('mandara_progress__B5_result'),
               B6_result=Sum('mandara_progress__B6_result'),
               B7_result=Sum('mandara_progress__B7_result'),
               B8_result=Sum('mandara_progress__B8_result'),
               C1_result=Sum('mandara_progress__C1_result'),
               C2_result=Sum('mandara_progress__C2_result'),
               C3_result=Sum('mandara_progress__C3_result'),
               C4_result=Sum('mandara_progress__C4_result'),
               C5_result=Sum('mandara_progress__C5_result'),
               C6_result=Sum('mandara_progress__C6_result'),
               C7_result=Sum('mandara_progress__C7_result'),
               C8_result=Sum('mandara_progress__C8_result'),
               D1_result=Sum('mandara_progress__D1_result'),
               D2_result=Sum('mandara_progress__D2_result'),
               D3_result=Sum('mandara_progress__D3_result'),
               D4_result=Sum('mandara_progress__D4_result'),
               D5_result=Sum('mandara_progress__D5_result'),
               D6_result=Sum('mandara_progress__D6_result'),
               D7_result=Sum('mandara_progress__D7_result'),
               D8_result=Sum('mandara_progress__D8_result'),
               E1_result=Sum('mandara_progress__E1_result'),
               E2_result=Sum('mandara_progress__E2_result'),
               E3_result=Sum('mandara_progress__E3_result'),
               E4_result=Sum('mandara_progress__E4_result'),
               E5_result=Sum('mandara_progress__E5_result'),
               E6_result=Sum('mandara_progress__E6_result'),
               E7_result=Sum('mandara_progress__E7_result'),
               E8_result=Sum('mandara_progress__E8_result'),
               F1_result=Sum('mandara_progress__F1_result'),
               F2_result=Sum('mandara_progress__F2_result'),
               F3_result=Sum('mandara_progress__F3_result'),
               F4_result=Sum('mandara_progress__F4_result'),
               F5_result=Sum('mandara_progress__F5_result'),
               F6_result=Sum('mandara_progress__F6_result'),
               F7_result=Sum('mandara_progress__F7_result'),
               F8_result=Sum('mandara_progress__F8_result'),
               G1_result=Sum('mandara_progress__G1_result'),
               G2_result=Sum('mandara_progress__G2_result'),
               G3_result=Sum('mandara_progress__G3_result'),
               G4_result=Sum('mandara_progress__G4_result'),
               G5_result=Sum('mandara_progress__G5_result'),
               G6_result=Sum('mandara_progress__G6_result'),
               G7_result=Sum('mandara_progress__G7_result'),
               G8_result=Sum('mandara_progress__G8_result'),
               H1_result=Sum('mandara_progress__H1_result'),
               H2_result=Sum('mandara_progress__H2_result'),
               H3_result=Sum('mandara_progress__H3_result'),
               H4_result=Sum('mandara_progress__H4_result'),
               H5_result=Sum('mandara_progress__H5_result'),
               H6_result=Sum('mandara_progress__H6_result'),
               H7_result=Sum('mandara_progress__H7_result'),
               H8_result=Sum('mandara_progress__H8_result'),
            ).first()
        context['mandara'] = mandara
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.MandaraTotalMiddleware, name='dispatch')
class MandaraMasMasChart(TemplateView):
    template_name = "mandara/mandara_masmas_chart.html"
    form_class = forms.MandaraChartForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        today = datetime.date.today()
        user_id = self.request.POST.get("user_id")
        kwargs['form'] = self.form_class(self.request)
        mandaras = MandaraBase.objects.select_related('mandara_period').filter(company_id=company_id,mandara_period__end_date__gte=today,mandara_period__start_date__lte=today,flg_finished=True)
        if user_id is not None and user_id != '':
            mandaras = mandaras.filter(user_id=user_id)
        first_mandara = mandaras.first()
        results = MandaraProgress.objects.all().filter(mandara_base__in=mandaras).annotate(
            month=ExtractMonth('date'),
            year=ExtractYear('date')
        )
        data = {}
        for i in results:
            key = str(i.year) + '/' + str(i.month)
            if key not in data:
                data[key] = i.sum_result()
            else:
                data[key] += i.sum_result()
        list_month = []
        list_value = []
        for key, value in data.items():
            list_month.append(key)
            list_value.append(value)

        kwargs['data_month'] = list_month
        kwargs['data_value'] = list_value

        if first_mandara is not None:
            start = first_mandara.mandara_period.display_time_start
            end = first_mandara.mandara_period.display_time_end
            kwargs['start'] = start
            kwargs['end'] = end

        kwargs['title_header'] = "MASMASMANDARA"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context['form'] = form

        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.MandaraTotalMiddleware, name='dispatch')    
class MandaraCompletionTab(TemplateView):
    template_name = "mandara/mandara_completion_tab.html"
    form_class = forms.MandaraForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        kwargs['form'] = self.form_class(self.request)
        today = datetime.date.today()
        user_id = self.request.POST.get("user_id")
        mandaras = MandaraBase.objects.select_related('mandara_period').filter(company_id=company_id,mandara_period__end_date__lt=today,flg_finished=True)
        max_time = mandaras.order_by('-mandara_period__end_date').first()
        min_time = mandaras.order_by('mandara_period__start_date').first()
        if min_time is not None:
            kwargs['start'] = min_time.mandara_period.display_time_start
        if max_time is not None:
            kwargs['end'] = max_time.mandara_period.display_time_end
        if user_id is not None and user_id != '':
            kwargs['mandaras'] = mandaras.filter(user_id=user_id)
        kwargs['title_header'] = "MASMASMANDARA"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context['form'] = form

        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
@method_decorator(middlewares.MandaraTotalMiddleware, name='dispatch')
class MandaraCompletionTabDetail(TemplateView):
    template_name = "mandara/mandara_completion_tab_detail.html"

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        id = self.kwargs.get('id')
        get_mandara_detail = MandaraBase.objects.select_related('mandara_period').filter(company_id=company_id,id=id,flg_finished=True).annotate(
               A1_result=Sum('mandara_progress__A1_result'),
               A2_result=Sum('mandara_progress__A2_result'),
               A3_result=Sum('mandara_progress__A3_result'),
               A4_result=Sum('mandara_progress__A4_result'),
               A5_result=Sum('mandara_progress__A5_result'),
               A6_result=Sum('mandara_progress__A6_result'),
               A7_result=Sum('mandara_progress__A7_result'),
               A8_result=Sum('mandara_progress__A8_result'),
               B1_result=Sum('mandara_progress__B1_result'),
               B2_result=Sum('mandara_progress__B2_result'),
               B3_result=Sum('mandara_progress__B3_result'),
               B4_result=Sum('mandara_progress__B4_result'),
               B5_result=Sum('mandara_progress__B5_result'),
               B6_result=Sum('mandara_progress__B6_result'),
               B7_result=Sum('mandara_progress__B7_result'),
               B8_result=Sum('mandara_progress__B8_result'),
               C1_result=Sum('mandara_progress__C1_result'),
               C2_result=Sum('mandara_progress__C2_result'),
               C3_result=Sum('mandara_progress__C3_result'),
               C4_result=Sum('mandara_progress__C4_result'),
               C5_result=Sum('mandara_progress__C5_result'),
               C6_result=Sum('mandara_progress__C6_result'),
               C7_result=Sum('mandara_progress__C7_result'),
               C8_result=Sum('mandara_progress__C8_result'),
               D1_result=Sum('mandara_progress__D1_result'),
               D2_result=Sum('mandara_progress__D2_result'),
               D3_result=Sum('mandara_progress__D3_result'),
               D4_result=Sum('mandara_progress__D4_result'),
               D5_result=Sum('mandara_progress__D5_result'),
               D6_result=Sum('mandara_progress__D6_result'),
               D7_result=Sum('mandara_progress__D7_result'),
               D8_result=Sum('mandara_progress__D8_result'),
               E1_result=Sum('mandara_progress__E1_result'),
               E2_result=Sum('mandara_progress__E2_result'),
               E3_result=Sum('mandara_progress__E3_result'),
               E4_result=Sum('mandara_progress__E4_result'),
               E5_result=Sum('mandara_progress__E5_result'),
               E6_result=Sum('mandara_progress__E6_result'),
               E7_result=Sum('mandara_progress__E7_result'),
               E8_result=Sum('mandara_progress__E8_result'),
               F1_result=Sum('mandara_progress__F1_result'),
               F2_result=Sum('mandara_progress__F2_result'),
               F3_result=Sum('mandara_progress__F3_result'),
               F4_result=Sum('mandara_progress__F4_result'),
               F5_result=Sum('mandara_progress__F5_result'),
               F6_result=Sum('mandara_progress__F6_result'),
               F7_result=Sum('mandara_progress__F7_result'),
               F8_result=Sum('mandara_progress__F8_result'),
               G1_result=Sum('mandara_progress__G1_result'),
               G2_result=Sum('mandara_progress__G2_result'),
               G3_result=Sum('mandara_progress__G3_result'),
               G4_result=Sum('mandara_progress__G4_result'),
               G5_result=Sum('mandara_progress__G5_result'),
               G6_result=Sum('mandara_progress__G6_result'),
               G7_result=Sum('mandara_progress__G7_result'),
               G8_result=Sum('mandara_progress__G8_result'),
               H1_result=Sum('mandara_progress__H1_result'),
               H2_result=Sum('mandara_progress__H2_result'),
               H3_result=Sum('mandara_progress__H3_result'),
               H4_result=Sum('mandara_progress__H4_result'),
               H5_result=Sum('mandara_progress__H5_result'),
               H6_result=Sum('mandara_progress__H6_result'),
               H7_result=Sum('mandara_progress__H7_result'),
               H8_result=Sum('mandara_progress__H8_result'),
            ).first()
        
        # end_YYYYMM = get_mandara_detail.end_YYYYMM
        # start_YYYYMM = get_mandara_detail.start_YYYYMM

        # format_end_date = f'{end_YYYYMM[:4]} 年 {int(end_YYYYMM[4:])} 月'
        # format_start_date = f'{start_YYYYMM[:4]} 年 {int(start_YYYYMM[4:])} 月'

        month = datetime.date.today().strftime("%m")

        kwargs['get_mandara_detail'] = get_mandara_detail
        kwargs['format_end_date'] = get_mandara_detail.mandara_period.display_time_end
        kwargs['format_start_date'] = get_mandara_detail.mandara_period.display_time_start
        kwargs['month'] = month
        kwargs['title_header'] = "MASMASMANDARA"
        return kwargs

@method_decorator(login_required, name='dispatch')            
class Watasheet(TemplateView):
    template_name = "watasheet/watasheet.html"
    form_class = forms.WatasheetForm
    test = None

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id

        initial_values = {
            "flg_finished": False,
        }

        evaluation_period = get_object_or_404(
            WatasheetEvaluationPeriod,
            company_id=company_id,
            evaluation_start__lte=datetime.date.today(),
            evaluation_end__gte=datetime.date.today()
        )
        self.test = evaluation_period.id
        watasheet_questions = evaluation_period.watasheet_questions.prefetch_related(
            Prefetch(
                'watasheet_results',
                queryset=(
                    WatasheetResult.objects
                        .filter(evaluation_period_id=evaluation_period.id,user_id=user_id,company_id=company_id)
                )
            )
        ).all().annotate(
            answer_value=WatasheetResult.objects.filter(
                watasheet_question=OuterRef("pk"),
                evaluation_period_id=evaluation_period.id,
                company_id=company_id,
                user_id=user_id
            ).values('id')[:1]
        ).order_by('sort_no')
        watasheet_type_result = WatasheetTypeResult.objects.filter(evaluation_period_id=evaluation_period.id, company_id=company_id,user_id=user_id).first()
        obj_type = evaluation_period.watasheet_type_results.filter(user_id=user_id,company_id=company_id).first()
        if obj_type is not None:
            initial_values['flg_finished'] = obj_type.flg_finished

        company = Company.objects.filter(id=company_id).first()
        
        kwargs = super(Watasheet, self).get_context_data(**kwargs)
        kwargs['evaluation_period'] = evaluation_period
        kwargs['watasheet_questions'] = watasheet_questions
        kwargs['questions'] = list(divide_chunks(watasheet_questions, 3))
        kwargs['type_A'] = obj_type.watasheet_type_a if obj_type is not None else 0
        kwargs['type_B'] = obj_type.watasheet_type_b if obj_type is not None else 0
        kwargs['type_C'] = obj_type.watasheet_type_c if obj_type is not None else 0
        kwargs['type_D'] = obj_type.watasheet_type_d if obj_type is not None else 0
        kwargs['type_E'] = obj_type.watasheet_type_e if obj_type is not None else 0
        kwargs['type_F'] = obj_type.watasheet_type_f if obj_type is not None else 0
        kwargs['type_content'] = obj_type.watasheet_context if obj_type is not None else ''
        kwargs['disabled'] = 'disabled' if initial_values['flg_finished'] else ''
        kwargs['form'] = self.form_class(initial_values)
        kwargs['team_concept'] = company
        kwargs['watasheet_type_result'] = watasheet_type_result
        kwargs['title_header'] = "KNOW MY SELF"

        return kwargs

    def post(self, request, *args, **kwargs):
        context_get = self.get_context_data(**kwargs)
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        flg_finished = self.request.POST.get("flg_finished") or False
        questions = self.request.POST.getlist("questions")
        form = self.form_class(request.POST, instance=context_get["watasheet_type_result"])

        if self.request.POST.get("watasheet_context") is not None:

            WatasheetResult.objects.filter(evaluation_period_id=context_get["evaluation_period"].id, user_id=user_id).delete()
            bulk_list = list()
            types = {
                "A" : 0,
                "B" : 0,
                "C" : 0,
                "D" : 0,
                "E" : 0,
                "F" : 0,
            }
            for q in questions:
                question = next(
                    (obj for obj in context_get['watasheet_questions'] if int(obj.id) == int(q)),
                    None
                )
                if question is not None:
                    types[question.group] = int(types[question.group]) + 1
                    bulk_list.append(
                        WatasheetResult(
                            company_id=company_id,
                            user_id=user_id,
                            evaluation_period_id=context_get["evaluation_period"].id,
                            watasheet_question_id=q,
                        )
                    )

            bulk_msj = WatasheetResult.objects.bulk_create(bulk_list)
            
            if form.is_valid():
                watasheet_type_result=form.save(commit=False)
                watasheet_type_result.user_id = user_id
                watasheet_type_result.company_id = company_id
                watasheet_type_result.watasheet_type_a = types['A']
                watasheet_type_result.watasheet_type_b = types['B']
                watasheet_type_result.watasheet_type_c = types['C']
                watasheet_type_result.watasheet_type_d = types['D']
                watasheet_type_result.watasheet_type_e = types['E']
                watasheet_type_result.watasheet_type_f = types['F']
                watasheet_type_result.evaluation_period_id=context_get["evaluation_period"].id
                if form.cleaned_data['vision_1_year']:
                    watasheet_type_result.vision_1_year = jaconv.zenkaku2hankaku(str(form.cleaned_data['vision_1_year']))
                if form.cleaned_data['vision_5_years']:
                    watasheet_type_result.vision_5_years = jaconv.zenkaku2hankaku(str(form.cleaned_data['vision_5_years']))
                if form.cleaned_data['vision_10_years']:
                    watasheet_type_result.vision_10_years = jaconv.zenkaku2hankaku(str(form.cleaned_data['vision_10_years']))
                watasheet_type_result.save()
                
        else:
            obj = WatasheetTypeResult.objects.update_or_create(
                company_id=company_id,
                user_id=user_id,
                evaluation_period_id=context_get["evaluation_period"].id,
                defaults={
                    "flg_finished": bool(flg_finished),
                }
            )
        context = self.get_context_data(**kwargs)
        context["message"] = '-- 保存しました。--'
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')            
class WatasheetType(TemplateView):
    template_name = "watasheet/watasheet_type.html"
    form_class = forms.WatasheetTypeForm
    test = None

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['watasheet_type_result'] = None
        kwargs['form'] = self.form_class(self.request)
        kwargs['title_header'] = "KNOW MY SELF"
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user_id = self.request.POST.get('user_id')
        evaluation_unit_id = self.request.POST.get('evaluation_unit')
        company_id = self.request.user.company_id

        watasheet_questions = WatasheetQuestion.objects.prefetch_related(
            Prefetch(
                'watasheet_results',
                queryset=(
                    WatasheetResult.objects
                        .filter(evaluation_period_id=evaluation_unit_id, user_id=user_id)
                )
            )
        ).all().annotate(
            answer_value=WatasheetResult.objects.filter(
                watasheet_question=OuterRef("pk"),
                evaluation_period_id=evaluation_unit_id,
                user_id=user_id
            ).values('id')[:1]
        ).order_by('sort_no')

        obj_type = WatasheetTypeResult.objects.filter(evaluation_period_id=evaluation_unit_id, user_id=user_id, flg_finished=True).first()
        team_concept = Company.objects.filter(id=company_id).first()

        kwargs = super().get_context_data(**kwargs)
        context['watasheet_questions'] = watasheet_questions
        context['questions'] = list(divide_chunks(watasheet_questions, 3))
        context['type_A'] = obj_type.watasheet_type_a if obj_type is not None else 0
        context['type_B'] = obj_type.watasheet_type_b if obj_type is not None else 0
        context['type_C'] = obj_type.watasheet_type_c if obj_type is not None else 0
        context['type_D'] = obj_type.watasheet_type_d if obj_type is not None else 0
        context['type_E'] = obj_type.watasheet_type_e if obj_type is not None else 0
        context['type_F'] = obj_type.watasheet_type_f if obj_type is not None else 0
        context['type_content'] = obj_type.watasheet_context if obj_type is not None else ''
        context['form'] = self.form_class(request, request.POST)
        context['watasheet_type_result'] = obj_type
        context['team_concept'] = team_concept

        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')            
class WatasheetImage(TemplateView):
    template_name = "watasheet/watasheet_image.html"