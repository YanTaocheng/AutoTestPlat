from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from . import models
import json


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:  # 确保用户名和密码都不为空
            #print('输入username: %s /n输入password：%s'%(username, password))
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    return HttpResponse(json.dumps({'status':'success','username':username}))
                else:
                    return HttpResponse(json.dumps({'status':'error'}))
            except:
                return HttpResponse(json.dumps({'status':'error'}))

        return HttpResponse(json.dumps({'status':'empty'}))
    
def logout(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

# Create your views here.
