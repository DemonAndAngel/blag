from django.db import models


# Create your models here.


class File(models.Model):
    s_file_name = models.CharField('源文件名', max_length=500,null=True)
    content_type = models.CharField('类型', max_length=50)
    size = models.IntegerField('文件大小', null=True)
    file_name = models.CharField('文件名', max_length=500)
    save_path = models.CharField('存储路径', max_length=1024)
    driver = models.CharField('驱动', max_length=50, default='local')
    used_at = models.DateTimeField('使用时间', null=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改日期', auto_now=True)


class User(models.Model):
    account = models.CharField('账号', max_length=20, unique=True)
    nickname = models.CharField('昵称', max_length=100)
    password = models.CharField('密码', max_length=200)
    salt = models.CharField('密码随机字符串加密', max_length=5)
    avatar_file = models.OneToOneField(File, on_delete=models.CASCADE, default=None, null=True)
    lasted_at = models.DateTimeField('最后一次登录时间', null=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改日期', auto_now=True)


class Role(models.Model):
    name = models.CharField('角色名', max_length=50)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改日期', auto_now=True)
    users = models.ManyToManyField(User)


class Permission(models.Model):
    name = models.CharField('权限名', max_length=50)
    controller = models.CharField('权限对应控制器', max_length=100)
    mothod = models.CharField('权限对应方法', max_length=200)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改日期', auto_now=True)
    roles = models.ManyToManyField(Role)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 级联删除
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    weight = models.IntegerField('权重', default=0)
    pv = models.IntegerField('总浏览数', default=0)
    uv = models.IntegerField('总用户浏览数', default=0)
    uv_ip_json = models.TextField('用户ip的json数组', null=True)
    lasted_at = models.DateTimeField('最新修改时间', auto_now_add=True)
    browsed_at = models.DateTimeField('最新浏览时间', auto_now_add=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改日期', auto_now=True)


class BlogBrowse(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)  # 级联删除
    pv = models.IntegerField('浏览数', default=0)
    uv = models.IntegerField('用户浏览数', default=0)
    uv_ip_json = models.TextField('用户ip的json数组', null=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改日期', auto_now=True)
