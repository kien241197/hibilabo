from . import forms
from .models import User, HonneQuestion, HonneTypeResult, HonneIndexResult, HonneQuestion, HonneAnswerResult, HonneEvaluationPeriod, Company, SelfcheckEvaluationPeriod, SelfcheckAnswerResult, SelfcheckQuestion, SelfcheckTypeResult, SelfcheckIndexResult, BonknowEvaluationPeriod, ResponsAnswer, ThinkAnswer, ResponsResult, ThinkResult, MandaraBase, MandaraProgress
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
from django.db.models.functions import ExtractMonth, ExtractYear, ExtractDay
from .constants import SELFCHECK_ANSWER, CIRCL, SQUARE, TRAIANGLE
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

User = get_user_model()
# wkhtml_to_pdf = os.path.join(
#     settings.BASE_DIR, "wkhtmltopdf.exe")
wkhtml_to_pdf = '/usr/bin/wkhtmltopdf'
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["period_honne"] = HonneEvaluationPeriod.objects.all().filter(evaluation_start__lte=datetime.date.today(),evaluation_end__gte=datetime.date.today()).first()
        context["period_selfcheck"] = SelfcheckEvaluationPeriod.objects.all().filter(evaluation_start__lte=datetime.date.today(),evaluation_end__gte=datetime.date.today()).first()
        context["period_bonknow"] = BonknowEvaluationPeriod.objects.all().filter(evaluation_start__lte=datetime.date.today(),evaluation_end__gte=datetime.date.today()).first()
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
class HonneSheet(LoginRequiredMixin, TemplateView):
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
        ).filter(apply_start_date__lte=datetime.date.today(),apply_end_date__gte=datetime.date.today()).order_by('sort_no')

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

class HonneTotal(LoginRequiredMixin, TemplateView):
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

class HonneTypeStaticks(LoginRequiredMixin, TemplateView):
    template_name = "honne/honne_type_staticks.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneTypeStaticks, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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

class HonneTypePersonalGraph(LoginRequiredMixin, TemplateView):
    template_name = "honne/honne_type_personal_graph.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneTypePersonalGraph, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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

class HonneIndexStaticks(LoginRequiredMixin, TemplateView):
    template_name = "honne/honne_index_staticks.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneIndexStaticks, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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

class HonneChart(LoginRequiredMixin, TemplateView):
    template_name = "honne/honne_chart.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneChart, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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

class HonneQrStaticks(LoginRequiredMixin, TemplateView):
    template_name = "honne/honne_qr_staticks.html"
    form_class = forms.HonneEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(HonneQrStaticks, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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
class SelfcheckIndex(LoginRequiredMixin, TemplateView):
    template_name = "selfcheck/selfcheck_index.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckIndex, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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

class SelfcheckIndexChart(LoginRequiredMixin, TemplateView):
    template_name = "selfcheck/selfcheck_index_chart.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckIndexChart, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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

class SelfcheckQuestions(LoginRequiredMixin, TemplateView):
    template_name = "selfcheck/selfcheck_questions.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckQuestions, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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

class SelfcheckType(LoginRequiredMixin, TemplateView):
    template_name = "selfcheck/selfcheck_type.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckType, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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

class SelfcheckTypeChart(LoginRequiredMixin, TemplateView):
    template_name = "selfcheck/selfcheck_type_chart.html"
    form_class = forms.SelfcheckEvaluationUnitForm

    def get_context_data(self, **kwargs):
        kwargs = super(SelfcheckTypeChart, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request)
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

class SelfcheckSheet(LoginRequiredMixin, TemplateView):
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

        selfcheck_questions = evaluation_period.selfcheck_questions.prefetch_related(
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
        ).order_by('sort_no')

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
class BonknowSheet(LoginRequiredMixin, TemplateView):
    template_name = "bonknow/bonknow_sheet.html"

    def get_context_data(self, **kwargs):
        evaluation_unit = self.kwargs['evaluationUnit']
        company_id = self.request.user.company_id
        user_id = self.request.user.id
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
        ).filter(apply_start_date__lte=datetime.date.today(),apply_end_date__gte=datetime.date.today()).order_by('sort_no')

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
        ).filter(apply_start_date__lte=datetime.date.today(),apply_end_date__gte=datetime.date.today()).order_by('sort_no')

        kwargs = super(BonknowSheet, self).get_context_data(**kwargs)
        kwargs['evaluation_unit'] = evaluation_unit
        kwargs['respons_questions'] = respons_questions
        kwargs['think_questions'] = think_questions
        kwargs['think_list'] = list(think_questions.values_list('id', flat=True))
        kwargs['res_list'] = list(respons_questions.values_list('id', flat=True))
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
        obj = ResponsResult.objects.update_or_create(
            company_id=company_id,
            user_id=user_id,
            evaluation_period_id=key_evaluation_unit,
            defaults={
                "logic": logic,
                "sense": sense,
                "review_date": datetime.date.today(),
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
                "review_date": datetime.date.today(),
            }
        )

        context = self.get_context_data(**kwargs)
        context["message"] = '-- 保存しました。--'

        return self.render_to_response(context)


class BonknowRespons(LoginRequiredMixin, TemplateView):
    template_name = "bonknow/bonknow_respons.html"
    form_class = forms.BonknowForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id

        kwargs = super(BonknowRespons, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request.GET or None)
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        context["form"] = form
        start_time = request.POST['start']
        end_time = request.POST['end']
        results = ResponsResult.objects.all().filter(company_id=request.user.company_id,user_id=request.user.id).order_by('review_date')
        if start_time != '':
            start_format = datetime.datetime.strptime(start_time + '-01', "%Y-%m-%d").date()
            results = results.filter(review_date__gte=start_format)
        if end_time != '':
            convert = list(end_time.split("-"))
            days = calendar.monthrange(int(convert[0]), int(convert[1]))
            end_format = datetime.datetime.strptime(end_time + '-' + str(days[1]), "%Y-%m-%d").date()
            results = results.filter(review_date__lte=end_format)
        context['times'] = [];
        context['logic'] = [];
        context['sense'] = [];
        for result in results:
            str_time = result.review_date.strftime('%Y/%m')
            context['times'].append(str_time)
            context['logic'].append(result.logic)
            context['sense'].append(result.sense)

        return self.render_to_response(context)

class BonknowThink(LoginRequiredMixin, TemplateView):
    template_name = "bonknow/bonknow_think.html"
    form_class = forms.BonknowForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id

        kwargs = super(BonknowThink, self).get_context_data(**kwargs)
        kwargs['form'] = self.form_class(self.request.GET or None)
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        context["form"] = form
        start_time = request.POST['start']
        end_time = request.POST['end']
        results = ThinkResult.objects.all().filter(company_id=request.user.company_id,user_id=request.user.id).order_by('review_date')
        if start_time != '':
            start_format = datetime.datetime.strptime(start_time + '-01', "%Y-%m-%d").date()
            results = results.filter(review_date__gte=start_format)
        if end_time != '':
            convert = list(end_time.split("-"))
            days = calendar.monthrange(int(convert[0]), int(convert[1]))
            end_format = datetime.datetime.strptime(end_time + '-' + str(days[1]), "%Y-%m-%d").date()
            results = results.filter(review_date__lte=end_format)
        context['times'] = [];
        context['must'] = [];
        context['want'] = [];
        for result in results:
            str_time = result.review_date.strftime('%Y/%m')
            context['times'].append(str_time)
            context['must'].append(result.must)
            context['want'].append(result.want)

        return self.render_to_response(context)

#MASMASMANDARA
class MandaraCreate(LoginRequiredMixin, TemplateView):
    template_name = "mandara/mandara_create.html"
    form_class = forms.MandaraCreateForm

    def get_context_data(self, **kwargs):
        today = datetime.date.today().strftime("%Y%m")
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        mandara = MandaraBase.objects.all().filter(
            user_id=user_id,company_id=company_id,start_YYYYMM__gt=today
        ).order_by('start_YYYYMM').first()

        kwargs['form'] = self.form_class(instance=mandara)
        kwargs['mandara'] = mandara

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
        if start_YYYYMM == '' or end_YYYYMM == '':
            context["message"] = '-- 目標期間は 1 年。--'
            return self.render_to_response(context)

        form.fields['start_YYYYMM'].choices = [(start_YYYYMM, start_YYYYMM)]
        form.fields['end_YYYYMM'].choices = [(end_YYYYMM, end_YYYYMM)]
        diff = int(end_YYYYMM) - int(start_YYYYMM)
        check_exists = MandaraBase.objects.filter(user_id=user_id,company_id=company_id,end_YYYYMM__gte=start_YYYYMM).exists()
        if context["mandara"] is not None:
            check_exists = MandaraBase.objects.filter(user_id=user_id,company_id=company_id,end_YYYYMM__gte=start_YYYYMM).exclude (pk=context["mandara"].id).exists()
        if check_exists:
            context["message"] = '-- マンダラの期限が重複しているため、作成できません。--'
            return self.render_to_response(context)

        if diff != 99:
            context["message"] = '-- 目標期間は 1 年。--'
            return self.render_to_response(context)

        if form.is_valid():
            mandara = form.save(commit=False)
            mandara.user_id = user_id
            mandara.company_id = company_id
            mandara.save()
            if context["mandara"] is not None:
                MandaraProgress.objects.filter(mandara_base_id=context["mandara"].id).delete()
            sdate = datetime.date(int(start_YYYYMM[0:4]), int(start_YYYYMM[4:6]), 1)   # start date
            edate = datetime.date(int(end_YYYYMM[0:4]), int(end_YYYYMM[4:6]) + 1, 1)   # end date
            delta = edate - sdate
            bulk_list = list()
            for i in range(delta.days):
                day = sdate + datetime.timedelta(days=i)
                bulk_list.append(
                    MandaraProgress(date=day, mandara_base_id=mandara.id)
                )

            bulk_msj = MandaraProgress.objects.bulk_create(bulk_list)
            context["message"] = '-- 保存しました。--'
            context["message_class"] = 'text-success'
        else:
            context["message"] = form.errors.as_data()

        return self.render_to_response(context)

    
class MandaraSheet(LoginRequiredMixin, TemplateView):
    template_name = "mandara/mandara_sheet.html"

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id

        return kwargs
    
    
class MandaraReuse(LoginRequiredMixin, TemplateView):
    template_name = "mandara/mandara_reuse.html"

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        today = datetime.date.today().strftime("%Y%m")
        mandara = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,end_YYYYMM__gte=today,start_YYYYMM__lte=today).annotate(
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
        kwargs['mandara'] = mandara
        kwargs['month'] = datetime.date.today().strftime("%m")
        if mandara is not None:
            kwargs['check_today'] = MandaraProgress.objects.all().filter(mandara_base_id=mandara.id,date=datetime.date.today()).first()
            results = MandaraProgress.objects.all().filter(mandara_base_id=mandara.id,date__lte=datetime.date.today()).annotate(
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
            
            kwargs['fix'] = True
            if mandara.start_YYYYMM > today:
                kwargs['fix'] = False

            start = mandara.start_YYYYMM[0:4] + '年' + mandara.start_YYYYMM[4:6] + '月'
            end = mandara.end_YYYYMM[0:4] + '年' + mandara.end_YYYYMM[4:6] + '月'
            kwargs['start'] = start
            kwargs['end'] = end

        return kwargs

class MandaraCompletion(LoginRequiredMixin, TemplateView):
    template_name = "mandara/mandara_completion.html"
    form_class = forms.MandaraCompleteForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        today_str = datetime.date.today().strftime("%Y%m")
        mandara_get = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,end_YYYYMM__lt=today_str).order_by('start_YYYYMM')

        kwargs['mandara_get'] = mandara_get
        kwargs['form'] = self.form_class()
        return kwargs
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        context["form"] = form
        start_YYYYMM = request.POST.get('start')
        end_YYYYMM = request.POST.get('end')
        
        if start_YYYYMM:
            context['mandara_get'] = context['mandara_get'].filter(start_YYYYMM__gte=start_YYYYMM)
        if end_YYYYMM:
            context['mandara_get'] = context['mandara_get'].filter(end_YYYYMM__lte=end_YYYYMM)
        return self.render_to_response(context)

    
class MandaraCompletionDetail(LoginRequiredMixin, TemplateView):
    template_name = "mandara/mandara_completion_detail.html"

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        id = self.kwargs.get('id')
        get_mandara_detail = MandaraBase.objects.filter(user_id=user_id,company_id=company_id,id=id).annotate(
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
        
        end_YYYYMM = get_mandara_detail.end_YYYYMM
        start_YYYYMM = get_mandara_detail.start_YYYYMM

        format_end_date = f'{end_YYYYMM[:4]} 年 {int(end_YYYYMM[4:])} 月'
        format_start_date = f'{start_YYYYMM[:4]} 年 {int(start_YYYYMM[4:])} 月'

        month = datetime.date.today().strftime("%m")

        kwargs['get_mandara_detail'] = get_mandara_detail
        kwargs['format_end_date'] = format_end_date
        kwargs['format_start_date'] = format_start_date
        kwargs['month'] = month
        
        return kwargs

@login_required
def get_detail_month(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            try:
                company_id = request.user.company_id
                user_id = request.user.id
                today_str = datetime.date.today().strftime("%Y%m")
                year = datetime.date.today().strftime("%Y")
                month = datetime.date.today().strftime("%m")
                box = request.GET['type_box']
                mandara_get = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,end_YYYYMM__gt=today_str).order_by('start_YYYYMM').first()
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
                today_str = datetime.date.today().strftime("%Y%m")
                data = json.load(request)
                todo = data.get('box')
                field = todo + '_result'
                mandara_get = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,end_YYYYMM__gt=today_str).order_by('start_YYYYMM').first()
                if mandara_get is not None:
                    today_progress = MandaraProgress.objects.filter(mandara_base_id=mandara_get.id,date=datetime.date.today())
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
        'javascript-delay': 200,
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

class MandaraPersonal(LoginRequiredMixin, TemplateView):
    template_name = "mandara/mandara_personal.html"
    form_class = forms.MandaraForm

    def get_context_data(self, **kwargs):
        kwargs['form'] = self.form_class(self.request)

        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context["form"] = form
        company_id = self.request.user.company_id
        user_id = self.request.POST.get("user_id")

        today = datetime.date.today().strftime("%Y%m")
        mandara = MandaraBase.objects.all().filter(user_id=user_id,company_id=company_id,end_YYYYMM__gte=today,start_YYYYMM__lte=today).annotate(
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

class MandaraMasMasChart(LoginRequiredMixin, TemplateView):
    template_name = "mandara/mandara_masmas_chart.html"
    form_class = forms.MandaraChartForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        today = datetime.date.today().strftime("%Y%m")
        user_id = self.request.POST.get("user_id")
        kwargs['form'] = self.form_class(self.request)
        mandaras = MandaraBase.objects.filter(company_id=company_id,end_YYYYMM__gte=today,start_YYYYMM__lte=today)
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
            start = first_mandara.start_YYYYMM[0:4] + '年' + first_mandara.start_YYYYMM[4:6] + '月'
            end = first_mandara.end_YYYYMM[0:4] + '年' + first_mandara.end_YYYYMM[4:6] + '月'
            kwargs['start'] = start
            kwargs['end'] = end

        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context['form'] = form

        return self.render_to_response(context)
    
class MandaraCompletionTab(LoginRequiredMixin, TemplateView):
    template_name = "mandara/mandara_completion_tab.html"
    form_class = forms.MandaraForm

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        kwargs['form'] = self.form_class(self.request)
        today = datetime.date.today().strftime("%Y%m")
        user_id = self.request.POST.get("user_id")
        mandaras = MandaraBase.objects.filter(company_id=company_id,end_YYYYMM__lt=today)
        max_time = mandaras.order_by('-end_YYYYMM').first()
        min_time = mandaras.order_by('start_YYYYMM').first()
        if min_time is not None:
            start = min_time.start_YYYYMM[0:4] + '年' + min_time.start_YYYYMM[4:6] + '月'
            kwargs['start'] = start
        if max_time is not None:
            end = max_time.end_YYYYMM[0:4] + '年' + max_time.end_YYYYMM[4:6] + '月'
            kwargs['end'] = end
        if user_id is not None and user_id != '':
            kwargs['mandaras'] = mandaras.filter(user_id=user_id)

        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request, request.POST)
        context['form'] = form

        return self.render_to_response(context)

class MandaraCompletionTabDetail(LoginRequiredMixin, TemplateView):
    template_name = "mandara/mandara_completion_tab_detail.html"

    def get_context_data(self, **kwargs):
        company_id = self.request.user.company_id
        user_id = self.request.user.id
        id = self.kwargs.get('id')
        get_mandara_detail = MandaraBase.objects.filter(company_id=company_id,id=id).annotate(
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
        
        end_YYYYMM = get_mandara_detail.end_YYYYMM
        start_YYYYMM = get_mandara_detail.start_YYYYMM

        format_end_date = f'{end_YYYYMM[:4]} 年 {int(end_YYYYMM[4:])} 月'
        format_start_date = f'{start_YYYYMM[:4]} 年 {int(start_YYYYMM[4:])} 月'

        month = datetime.date.today().strftime("%m")

        kwargs['get_mandara_detail'] = get_mandara_detail
        kwargs['format_end_date'] = format_end_date
        kwargs['format_start_date'] = format_start_date
        kwargs['month'] = month
        
        return kwargs