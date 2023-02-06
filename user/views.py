from django.shortcuts import render, redirect
from django.contrib import auth

'''
登录
'''


def login_(request):
    # 防止用户利用django路径，在已经登录的情况下进入登录页
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, "login.html")


'''
注册
'''


def register_(request):
    return render(request, "register.html")


'''
退出登录
'''


def logout_(request):
    auth.logout(request)
    return redirect("/")
