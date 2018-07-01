from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_http_methods

import string
import random
import re
import logging

from util import common

from app.models import User


@require_http_methods(["POST"])
def loginHandle(request):
    postData = common.requestBodyData(request)
    account = postData.get('account', None)
    password = postData.get('password', None)
    if account == None or password == None:
        return HttpResponse(common.makeResponseJson({}, 408, '参数错误！'))
    # if (request.session.get('app_user_account', None) != None):
    #     return HttpResponse(common.makeResponseJson({}, 403, '用户已登录！'))
    try:
        user = User.objects.get(account=account)
    except User.DoesNotExist:
        return HttpResponse(common.makeResponseJson({}, 403, '账号未注册！'))
    password = password + user.salt
    if check_password(password, user.password):
        request.session['app_user_account'] = account
        return HttpResponse(common.makeResponseJson({}))
    else:
        return HttpResponse(common.makeResponseJson({}, 407, '账号密码错误！'))


@require_http_methods(["POST"])
def registerHandle(request):
    postData = common.requestBodyData(request)
    account = postData.get('account',None)
    nickname = postData.get('nickname',None)
    password = postData.get('password',None)
    if re.search(r'^[a-zA-Z0-9_-]{6,20}$', account) == None:
        return HttpResponse(common.makeResponseJson({}, 407, '账号格式有误！'))
    if re.search(r'^[a-zA-Z0-9_-]{6,20}$', password) == None:
        return HttpResponse(common.makeResponseJson({}, 407, '密码格式有误！'))
    try:
        user = User.objects.get(account=account)
    except User.DoesNotExist:
        # 添加用户
        salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        my_password = make_password(password + salt)
        user = User(account=account, nickname=nickname != None and nickname or account, password=my_password, salt=salt)
        user.save()
        # 这里需要写入角色权限
        return HttpResponse(common.makeResponseJson())
    return HttpResponse(common.makeResponseJson({}, 407, '账号已存在！'))
