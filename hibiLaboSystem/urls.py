from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
	path('', views.Home.as_view(), name='home'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('register-done/', views.RegisterSuccess.as_view(), name='register_done'),
    path('my-info/', login_required(views.MyInfo.as_view()), name='my_info'),
	path('my-info/edit/', login_required(views.InfoUpdate.as_view()), name='info_update'),
	path('my-info/edit-workinginfo/', login_required(views.UserUpdateWorkinginfo.as_view()), name='workinginfo_update'),
	path('my-info/password-change/', login_required(views.PasswordChange.as_view()), name='password_change'),
	path('my-info/password-change_done/', login_required(views.PasswordChangeDone.as_view()), name='password_change_done'),

	path('honne-sheet/<evaluationUnit>', login_required(views.HonneSheet.as_view()), name='honne_sheet'),
	path('honne-total', login_required(views.HonneTotal.as_view()), name='honne_total'),
	path('honne-type-staticks', login_required(views.HonneTypeStaticks.as_view()), name='honne_type_staticks'),
	path('honne-index-staticks', login_required(views.HonneIndexStaticks.as_view()), name='honne_index_staticks'),
	path('honne-chart', login_required(views.HonneChart.as_view()), name='honne_chart'),
	path('honne-qr-staticks', login_required(views.HonneQrStaticks.as_view()), name='honne_qr_staticks'),
	path('honne-type-personal-graph', login_required(views.HonneTypePersonalGraph.as_view()), name='honne_type_personal_graph'),

	path('selfcheck-sheet/<evaluationUnit>', login_required(views.SelfcheckSheet.as_view()), name='selfcheck_sheet'),
	path('selfcheck-type', login_required(views.SelfcheckType.as_view()), name='selfcheck_type'),
	path('selfcheck-type-chart', login_required(views.SelfcheckTypeChart.as_view()), name='selfcheck_type_chart'),
	path('selfcheck', login_required(views.SelfcheckIndex.as_view()), name='selfcheck_index'),
	path('selfcheck-index-chart', login_required(views.SelfcheckIndexChart.as_view()), name='selfcheck_index_chart'),
	path('selfcheck-questions', login_required(views.SelfcheckQuestions.as_view()), name='selfcheck_questions'),

	path('bonknow-sheet/<evaluationUnit>', login_required(views.BonknowSheet.as_view()), name='bonknow_sheet'),
	path('bonknow-think', login_required(views.BonknowThink.as_view()), name='bonknow_think'),
	path('bonknow-respons', login_required(views.BonknowRespons.as_view()), name='bonknow_respons'),

	path('mandara', login_required(views.Mandara.as_view()), name='mandara'),
]