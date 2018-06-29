"""blag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.conf.urls import url
from app.controller import index
from app.controller import user
from app.api import user as apiUser

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    # 首页
    path('', index.index, name='index'),
    path('/', index.index, name='index'),
    path('index/', index.index, name='index'),

    # 登录
    path('login/', user.login, name='login'),
    # 注册
    path('register/', user.register, name='register'),

    # 接口
    path('api/loginHandle/', apiUser.loginHandle, name='loginHandle'),
    path('api/registerHandle/', apiUser.registerHandle, name='registerHandle'),
]
