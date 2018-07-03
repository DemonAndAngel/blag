import json
import math
from app.models import User


def pageInfo(title):
    return {'title': title}


# 搞不懂
def querySetToDict(querySet, callback=None):
    data = []
    for set in querySet:
        sData = {}
        if callback is not None:
            sData = callback(set, querySet[set])
        else:
            for s in querySet[set]:
                sData[s] = querySet[set][s]
        data.append(sData)
    return data


def makeResponseJson(data={}, code=0, msg='success', red=''):
    data = {
        'meta': {
            'code': code,
            'msg': msg,
        },
        'data': data
    }
    if red:
        data['meta']['red'] = red
    return json.dumps(data, ensure_ascii=False, indent=2)


def makeResponseJsonWithPageInfo(page=1, size=10, total=0, data={}, code=0, msg='success', red=''):
    data['page_info'] = {
        'page': page,
        'size': size,
        'total': total,
        'total_page': math.ceil(total / size)
    }
    return makeResponseJson(data, code, msg, red)


def requestBodyData(request):
    return json.loads(request.body)


def nowLoginUser(request):
    account = request.session.get('app_user_account', None)
    if account is None:
        return None
    else:
        try:
            user = User.objects.get(account=account)
            return user
        except User.DoesNotExist:
            return None


def ip(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip


