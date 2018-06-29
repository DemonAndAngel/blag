from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
	account = models.CharField('账号',max_length=20,unique=True)
	nickname = models.CharField('昵称',max_length=100)
	password = models.CharField('密码',max_length=200)
	salt = models.CharField('密码随机字符串加密',max_length=5)
	lasted_at = models.DateTimeField('最后一次登录时间',null = True)
	created_at = models.DateTimeField('创建时间',auto_now_add = True)
	updated_at = models.DateTimeField('最后修改日期', auto_now = True)

class Role(models.Model):
	name = models.CharField('角色名',max_length=50)
	created_at = models.DateTimeField('创建时间',auto_now_add = True)
	updated_at = models.DateTimeField('最后修改日期', auto_now = True)
	users = models.ManyToManyField(User)

class Permission(models.Model):
	name = models.CharField('权限名',max_length=50)
	controller = models.CharField('权限对应控制器',max_length=100)
	mothod = models.CharField('权限对应方法',max_length=200)
	created_at = models.DateTimeField('创建时间',auto_now_add = True)
	updated_at = models.DateTimeField('最后修改日期', auto_now = True)
	roles = models.ManyToManyField(Role)
