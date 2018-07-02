from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class Auth(MiddlewareMixin):
    def process_request(self, request):
        not_login = [
            'admin',
            'blog/index',
            'blog/register',
            'blog/login',
            'api/loginHandle',
            'api/registerHandle'
        ]
        for name in not_login:
            if name in request.path:
                return None
        return HttpResponseForbidden('没有权限')
