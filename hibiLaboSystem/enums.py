from enum import Enum


class RoleEnum(Enum):

	日々研 = 90
	Partner = 40
	Company_Admin = 30
	Company_Director = 25
	Company_SuperVisor = 20
	Company_Staff = 10
	@classmethod
	def choices(cls):
		return [(i, i.value) for i in cls]

class RolePermission(Enum):

	日々研 = 'Super_user'
	Partner = [
		"add_company", "change_company", "delete_company", "view_company",
		"add_branch", "change_branch", "delete_branch", "view_branch",
		"add_user", "change_user", "delete_user", "view_user",
		"add_honnequestion", "change_honnequestion", "delete_honnequestion", "view_honnequestion",
		"add_responsquestion", "change_responsquestion", "delete_responsquestion", "view_responsquestion",
		"add_selfcheckquestion", "change_selfcheckquestion", "delete_selfcheckquestion", "view_selfcheckquestion",
		"add_thinkquestion", "change_thinkquestion", "delete_thinkquestion", "view_thinkquestion",
		"add_watasheetquestion", "change_watasheetquestion", "delete_watasheetquestion", "view_watasheetquestion",
		"add_bonknowevaluationperiod", "change_bonknowevaluationperiod", "delete_bonknowevaluationperiod", "view_bonknowevaluationperiod",
		"add_honneevaluationperiod", "change_honneevaluationperiod", "delete_honneevaluationperiod", "view_honneevaluationperiod",
		"add_selfcheckevaluationperiod", "change_selfcheckevaluationperiod", "delete_selfcheckevaluationperiod", "view_selfcheckevaluationperiod",
		"add_mandaraperiod", "change_mandaraperiod", "delete_mandaraperiod", "view_mandaraperiod",
		"add_watasheetevaluationperiod", "change_watasheetevaluationperiod", "delete_watasheetevaluationperiod", "view_watasheetevaluationperiod",
	]
	Company_Admin = [
		"change_company", "view_company",
		"add_branch", "change_branch", "delete_branch", "view_branch",
		"change_user", "view_user",
		"add_bonknowevaluationperiod", "change_bonknowevaluationperiod", "delete_bonknowevaluationperiod", "view_bonknowevaluationperiod",
		"add_honneevaluationperiod", "change_honneevaluationperiod", "delete_honneevaluationperiod", "view_honneevaluationperiod",
		"add_selfcheckevaluationperiod", "change_selfcheckevaluationperiod", "delete_selfcheckevaluationperiod", "view_selfcheckevaluationperiod",
		"add_mandaraperiod", "change_mandaraperiod", "delete_mandaraperiod", "view_mandaraperiod",
		"add_watasheetevaluationperiod", "change_watasheetevaluationperiod", "delete_watasheetevaluationperiod", "view_watasheetevaluationperiod",
		"change_honnetyperesult", "view_honnetyperesult",
		"change_selfchecktyperesult", "view_selfchecktyperesult",
		"change_watasheettyperesult", "view_watasheettyperesult",
		"change_responsresult", "view_responsResult",
		"change_mandarabase", "view_mandarabase"

	]
	Company_Director = [
		"change_company", "view_company",
		"add_branch", "change_branch", "delete_branch", "view_branch",
		"change_user", "view_user",
		"add_bonknowevaluationperiod", "change_bonknowevaluationperiod", "delete_bonknowevaluationperiod", "view_bonknowevaluationperiod",
		"add_honneevaluationperiod", "change_honneevaluationperiod", "delete_honneevaluationperiod", "view_honneevaluationperiod",
		"add_selfcheckevaluationperiod", "change_selfcheckevaluationperiod", "delete_selfcheckevaluationperiod", "view_selfcheckevaluationperiod",
		"add_mandaraperiod", "change_mandaraperiod", "delete_mandaraperiod", "view_mandaraperiod",
		"add_watasheetevaluationperiod", "change_watasheetevaluationperiod", "delete_watasheetevaluationperiod", "view_watasheetevaluationperiod",
	]
	Company_SuperVisor = [
		"add_user", "change_user", "delete_user", "view_user",
	]
	Company_Staff = []
