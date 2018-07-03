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
from django.urls import path, re_path
# from django.conf.urls import url
from app.controller import index
from app.api import user as apiUser
from app.api import blog as apiBlog
from app.api import file as apiFile

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    # 首页
    path('', index.index),
    path('/', index.index),
    # 博客前端路由
    path('blog/', index.index),
    # 接口
    # 用户登录接口
    path('api/login/handle/', apiUser.loginHandle, name='loginHandle'),
    path('api/logout/handle/', apiUser.logoutHandle, name='logoutHandle'),
    path('api/register/handle/', apiUser.registerHandle, name='registerHandle'),

    # 博客帖子接口
    path('api/get/blog/handle/', apiBlog.getHandle, name='getBlogHandle'),
    path('api/get/blog/list/handle/', apiBlog.getListHandle, name='getBlogListHandle'),
    path('api/add/blog/handle/', apiBlog.addHandle, name='addBlogHandle'),
    path('api/edit/blog/handle/', apiBlog.editHandle, name='editBlogHandle'),
    path('api/del/blog/handle/', apiBlog.deleteHandle, name='delBlogHandle'),

    # 上传文件接口
    path('api/upload/file/handle/', apiFile.uploadFileHandle, name='uploadFileHandle')
]
