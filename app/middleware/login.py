from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class Auth(MiddlewareMixin):
    def process_request(self, request):
        not_login = [
            'admin',
            'blog/index',
            'blog/register',
            'blog/login',
            'api/login/handle',
            'api/register/handle',
            'api/get/blog/handle',
            'api/get/blog/list/handle',
            'api/upload/file/handle',
        ]
        for name in not_login:
            if name in request.path:
                return None
        if request.path == '' or request.path == '/':
            return None
        if request.session.get('app_user_account', None) is None:
            return HttpResponseForbidden('没有权限')
        return None
