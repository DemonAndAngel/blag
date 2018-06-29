from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class Auth(MiddlewareMixin):
    def process_request(self, request):
        not_login = [
            '/admin/',
            '/admin/login/',
            '/favicon.ico',
            '',
            '/',
            '/index/',
            '/login/',
            '/loginHandle/',
            '/register/',
            '/registerHandle/',
        ]
        for name in not_login:
            if name == request.path:
                return None
        return HttpResponseForbidden('没有权限')
