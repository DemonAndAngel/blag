from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from util import common

from app.models import Blog, BlogBrowse
import datetime
import json


@require_http_methods(['GET'])
def getHandle(request):
    blog_id = request.GET.get('blog_id', None)
    if blog_id is None:
        return common.makeResponseJson({}, 407, '参数错误！')
    try:
        blog = Blog.objects.get(id=blog_id)
        now = datetime.datetime.now()
        to = datetime.timedelta(days=1)
        ip = common.ip(request)
        try:
            blogBrowse = blog.blogbrowse_set.filter(created_at__range=[now, to]).first()
            blogBrowse.pv += 1
            if ip not in blogBrowse.uv_ip_json:
                blogBrowse.uv += 1
                uvIp = json.loads(blogBrowse.uv_ip_json)
                uvIp.append(ip)
                blogBrowse.uv_ip_json += json.dumps(uvIp, ensure_ascii=False, indent=2)
        except BlogBrowse.DoesNotExist:
            blogBrowse = BlogBrowse(pv=1, uv=1, blog=blog, uv_ip_json=json.dumps([ip], ensure_ascii=False, indent=2))
        blogBrowse.save()
        blog.pv += 1
        if ip not in blog.uv_ip_json:
            blog.uv += 1
            uvIp = json.loads(blog.uv_ip_json)
            uvIp.append(ip)
            blog.uv_ip_json += json.dumps(uvIp, ensure_ascii=False, indent=2)
        blog.save()
        data = {
            'blog': {
                'title': blog.title,
                'content': blog.content,
                'created_at': blog.created_at,
                'lasted_at': blog.lasted_at,
                'browsed_at': blog.browsed_at,
                'pv': blog.pv,
                'uv': blog.uv,
                'browse': {
                    'pv': blogBrowse.pv,
                    'uv': blogBrowse.uv,
                }
            }
        }
        return common.makeResponseJson(data)
    except Blog.DoesNotExist:
        return common.makeResponseJson({}, 404, '找不到对应数据！')


@require_http_methods(['GET'])
def getListHandle(request):
    page = request.GET.get('page', 1)
    size = request.GET.get('size', 10)
    if not page or int(page) < 1:
        page = 1
    if not size or int(size) < 1:
        size = 10
    start = (page - 1) * size
    end = page * size
    total = Blog.objects.order_by('-weight', '-uv', '-pv').count()
    try:
        blog = Blog.objects.order_by('-weight', '-uv', '-pv')[start:end].all()
    except Blog.DoesNotExist:
        blog = ''
    blogs = []
    for set in blog:
        user = set.user
        sData = {
            'title': set.title,
            'created_at': set.created_at.strftime('%Y-%m-%d %H:%S:%I'),
            'pv': set.pv,
            'uv': set.uv,
            'user': {
                'nickname': user.nickname
            }
        }
        blogs.append(sData)
    data = {
        'blog': blogs
    }
    return HttpResponse(common.makeResponseJsonWithPageInfo(page, size, total, data))


@require_http_methods(['POST'])
def addHandle(request):
    return common.makeResponseJson()


@require_http_methods(['PUT'])
def editHandle(request):
    return common.makeResponseJson()


@require_http_methods(['DELETE'])
def deleteHandle(request):
    return common.makeResponseJson()
