from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from util import common
from util import file as FileUtil


def uploadFileHandle(request):
    save_path = request.POST.get('save_path', '')
    file_obj = request.FILES['file']
    file = FileUtil.saveFile(file_obj, save_path=save_path)
    return HttpResponse(common.makeResponseJson({'id': file.id}))
    # postData = common.requestBodyData(request)
    # save_path = postData
