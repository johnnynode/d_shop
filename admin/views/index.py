from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 后台首页
def index(request):
    return render(request,"admin/index.html")

# 会员登录表单
def login(request):
    return render(request,'myadmin/login.html')

# 会员执行登录
def dologin(request):
    pass

# 会员退出
def logout(request):
    pass