from django.conf import settings
from app.models import File
import datetime
import os

BASE_PATH = '/static/blog/upload'
BASE_ALL_PATH = os.path.join(settings.BASE_DIR, 'static', 'blog', 'upload')


def getFileUrl(file, request):
    if file:
        return 'http://' + request.get_host() + file.save_path + file.file_name
    else:
        return ''


def saveFile(file_obj, save_path='', is_real=False):
    # 存储文件
    save_path = save_path.strip('/')
    open_path = BASE_ALL_PATH + '/' + save_path + '/'
    save_path = BASE_PATH + '/' + save_path + '/'
    if not os.path.exists(open_path):
        os.makedirs(open_path)
    f = open(open_path + file_obj.name, 'wb')
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()
    # 写入数据库
    file = File(s_file_name=file_obj.name, content_type=file_obj.content_type, size=file_obj.size,
                file_name=file_obj.name, save_path=save_path, driver='local')
    if is_real:
        file.used_at = datetime.datetime.now()
    file.save()
    return file
