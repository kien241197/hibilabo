from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin

class HonneMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        # if request.user.role_id not in [99, 20, 10]:
        #     raise PermissionDenied()
        return super().__call__(request)

class HonneTotalMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        if request.user.role_id not in [99, 20]:
            raise PermissionDenied()
        return super().__call__(request)

class SelfcheckMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        # if request.user.role_id not in [99, 20, 10]:
        #     raise PermissionDenied()
        return super().__call__(request)

class SelfcheckTotalMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        if request.user.role_id not in [99, 20]:
            raise PermissionDenied()
        return super().__call__(request)

class BonknowMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        # if request.user.role_id not in [99, 20, 10]:
        #     raise PermissionDenied()
        return super().__call__(request)

class BonknowTotalMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        if request.user.role_id not in [99, 20]:
            raise PermissionDenied()
        return super().__call__(request)

class MandaraMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        # if request.user.role_id not in [99, 20, 10, None]:
        #     raise PermissionDenied()
        return super().__call__(request)

class MandaraTotalMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        if request.user.role_id not in [99, 20]:
            raise PermissionDenied()
        return super().__call__(request)