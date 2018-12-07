from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<center>欢迎访问我的博客首页^_^</center>")
