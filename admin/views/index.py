from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 后台首页
def index(request):
    return render(request,"admin/index.html")