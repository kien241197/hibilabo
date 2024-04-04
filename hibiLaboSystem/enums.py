from enum import Enum


class RoleEnum(Enum):

	日々研 = 90
	Partner = 40
	Company_Admin = 30
	Company_SuperVisor = 20
	Company_Staff = 10
	@classmethod
	def choices(cls):
		return [(i, i.value) for i in cls]
