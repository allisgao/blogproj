from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("<center>欢迎访问我的博客首页^_^</center>")
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })