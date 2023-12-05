from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import PermissionDenied

class HonneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.role_id not in [99, 20, 10]:
            raise PermissionDenied()

        response = self.get_response(request)
        return response

class HonneTotalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.role_id not in [99, 20]:
            raise PermissionDenied()

        response = self.get_response(request)
        return response

class SelfcheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.role_id not in [99, 20, 10]:
            raise PermissionDenied()

        response = self.get_response(request)
        return response

class SelfcheckTotalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.role_id not in [99, 20]:
            raise PermissionDenied()

        response = self.get_response(request)
        return response

class BonknowMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.role_id not in [99, 20, 10]:
            raise PermissionDenied()

        response = self.get_response(request)
        return response

class BonknowTotalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.role_id not in [99, 20]:
            raise PermissionDenied()

        response = self.get_response(request)
        return response

class MandaraMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.role_id not in [99, 20, 10, None]:
            raise PermissionDenied()

        response = self.get_response(request)
        return response

class MandaraTotalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.role_id not in [99, 20]:
            raise PermissionDenied()

        response = self.get_response(request)
        return response