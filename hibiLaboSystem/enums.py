from enum import Enum


class RoleEnum(Enum):

	日々研 = "日々研"
	Partner = "Partner"
	Company_Admin = "Company Admin"
	Company_SuperVisor = "Company SuperVisor"
	Company_Staff = "Company Staff"
	@classmethod
	def choices(cls):
		return [(i, i.value) for i in cls]
