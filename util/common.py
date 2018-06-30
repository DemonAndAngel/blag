import json


def pageInfo(title):
    return {'title': title}


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


def requestBodyData(request):
    return json.loads(request.body)
