from django.shortcuts import render
from util import common

# Create your views here.
def login(request):
	context = {}
	context['pageInfo'] = common.pageInfo(title='登录页面')
	return render(request, 'user/login.html', context)
	
def register(request):
	context = {}
	context['pageInfo'] = common.pageInfo(title='注册页面')
	return render(request, 'user/register.html', context)

	