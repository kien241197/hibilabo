from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home.as_view(), name='home'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('register-done/', views.RegisterSuccess.as_view(), name='register_done'),
    path('my-info/', views.MyInfo.as_view(), name='my_info'),
	path('my-info/edit/', views.InfoUpdate.as_view(), name='info_update'),
	path('my-info/edit-workinginfo/', views.UserUpdateWorkinginfo.as_view(), name='workinginfo_update'),
	path('my-info/password-change/', views.PasswordChange.as_view(), name='password_change'),
	path('my-info/password-change_done/', views.PasswordChangeDone.as_view(), name='password_change_done'),

	path('honne-sheet/<evaluationUnit>', views.HonneSheet.as_view(), name='honne_sheet'),
	path('honne-total', views.HonneTotal.as_view(), name='honne_total'),
	path('honne-type-staticks', views.HonneTypeStaticks.as_view(), name='honne_type_staticks'),
	path('honne-index-staticks', views.HonneIndexStaticks.as_view(), name='honne_index_staticks'),
	path('honne-chart', views.HonneChart.as_view(), name='honne_chart'),
	path('honne-qr-staticks', views.HonneQrStaticks.as_view(), name='honne_qr_staticks'),
	path('honne-type-personal-graph', views.HonneTypePersonalGraph.as_view(), name='honne_type_personal_graph'),

	path('selfcheck-sheet/<evaluationUnit>', views.SelfcheckSheet.as_view(), name='selfcheck_sheet'),
	path('selfcheck-type', views.SelfcheckType.as_view(), name='selfcheck_type'),
	path('selfcheck-type-chart', views.SelfcheckTypeChart.as_view(), name='selfcheck_type_chart'),
	path('selfcheck', views.SelfcheckIndex.as_view(), name='selfcheck_index'),
	path('selfcheck-index-chart', views.SelfcheckIndexChart.as_view(), name='selfcheck_index_chart'),
	path('selfcheck-questions', views.SelfcheckQuestions.as_view(), name='selfcheck_questions'),

	path('bonknow-sheet/<evaluationUnit>', views.BonknowSheet.as_view(), name='bonknow_sheet'),
	path('bonknow-think', views.BonknowThink.as_view(), name='bonknow_think'),
	path('bonknow-respons', views.BonknowRespons.as_view(), name='bonknow_respons'),

	path('mandara', views.Mandara.as_view(), name='mandara'),
    path('masmasmandara', views.Masmasmandara.as_view(), name='masmasmandara'),
]