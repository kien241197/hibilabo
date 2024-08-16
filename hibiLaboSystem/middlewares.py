from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin
from .enums import RoleEnum

class BonknowMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        # if request.user.role is None or request.user.role.role not in [RoleEnum.日々研.value, RoleEnum.Company_SuperVisor.value, RoleEnum.Company_Staff.value]:
        #     raise PermissionDenied()
        return super().__call__(request)

class HonneMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        # if request.user.role is None or request.user.role.role not in [RoleEnum.日々研.value, RoleEnum.Company_SuperVisor.value, RoleEnum.Company_Staff.value]:
        #     raise PermissionDenied()
        return super().__call__(request)

class HonneTotalMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        if request.user.role is None or request.user.role.role not in [RoleEnum.Company_Admin.value, RoleEnum.Company_SuperVisor.value]:
            raise PermissionDenied()
        return super().__call__(request)

class SelfcheckMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        # if request.user.role is None or request.user.role.role not in [RoleEnum.日々研.value, RoleEnum.Company_SuperVisor.value, RoleEnum.Company_Staff.value]:
        #     raise PermissionDenied()
        return super().__call__(request)

class SelfcheckTotalMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        if request.user.role is None or request.user.role.role not in [RoleEnum.Company_Admin.value, RoleEnum.Company_SuperVisor.value]:
            raise PermissionDenied()
        return super().__call__(request)

class BonknowMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        # if request.user.role is None or request.user.role.role not in [RoleEnum.日々研.value, RoleEnum.Company_SuperVisor.value, RoleEnum.Company_Staff.value]:
        #     raise PermissionDenied()
        return super().__call__(request)

class BonknowTotalMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        if request.user.role is None or request.user.role.role not in [RoleEnum.Company_Admin.value, RoleEnum.Company_SuperVisor.value]:
            raise PermissionDenied()
        return super().__call__(request)

class MandaraMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        # if request.user.role is None or request.user.role.role not in [RoleEnum.日々研.value, RoleEnum.Company_SuperVisor.value, RoleEnum.Company_Staff.value, None]:
        #     raise PermissionDenied()
        return super().__call__(request)

class MandaraTotalMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        if request.user.role is None or request.user.role.role not in [RoleEnum.Company_Admin.value, RoleEnum.Company_SuperVisor.value]:
            raise PermissionDenied()
        return super().__call__(request)