def pageInfo(title):
	return {'title':title}

def makeResponseJson(data={},code=0,msg='success',red=''):
	import json
	data = {
		'meta': {
			'code': code,
			'msg': msg,
		},
		'data': data
	}
	if red:
		data['meta']['red'] = red
	return json.dumps(data,ensure_ascii=False,indent=2)