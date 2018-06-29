from django.shortcuts import render


# Create your views here.
def index(request):
    request.session.get('app_user_account', None)
    return render(request, 'index/index.html')
