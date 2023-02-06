'''
登录和注册
'''
import re
from .models import *
from datetime import datetime
from django.contrib.auth import login
from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

# email正则匹配字符串
email_match = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
# 密码安全检查正则匹配字符串
password_safe = r'^(?![A-Za-z]+$)(?![A-Z0-9]+$)(?![a-z0-9]+$)(?![a-z\W]+$)(?![A-Z\W]+$)(?![0-9\W]+$)[a-zA-Z0-9\W]{8,16}$'
'''
登录验证
'''


@csrf_exempt
def login_now(request):
    user = None  # 用户对象/登录验证对象
    vercode = None  # 邮箱密钥对象
    username = request.POST.get("username")
    password = request.POST.get("password")
    get_vercode = request.POST.get("vercode")
    # 防止用户恶意提交长数据
    if len(username) > 50 or len(password) > 50 or len(get_vercode) > 10:
        msg = '提交的信息过长，被后端拦截'
        return HttpResponse(msg)
    # 用户使用邮箱登录
    if re.match(email_match, username):
        try:
            user = get_user_by_email(username)
            user = login_blocking(user.username, password)
        except:
            pass
    # 用户使用用户名登录
    else:
        try:
            user = get_user_by_username(username)
            user = login_blocking(user.username, password)
        except:
            pass

    if user == None:
        msg = '用户名或密码或邮箱密钥错误'
        return HttpResponse(msg)
    else:
        try:
            vercode = get_vercode_by_username(user.username)
        except:
            pass
        now_time = datetime.now()
        str_d1 = now_time.strftime('%Y-%m-%d %H:%M:%S')
        str_d2 = vercode.last_modified.strftime('%Y-%m-%d %H:%M:%S')
        date_d1 = datetime.strptime(str_d1, '%Y-%m-%d %H:%M:%S')
        date_d2 = datetime.strptime(str_d2, '%Y-%m-%d %H:%M:%S')
        d = (date_d1 - date_d2).seconds
        if vercode.code != get_vercode:
            msg = '用户名或密码或邮箱密钥错误'
            return HttpResponse(msg)
        if d > 520:
            msg = '用户名或密码或邮箱密钥错误'
            return HttpResponse(msg)
        else:
            login(request, user)
            return HttpResponse('ok')


'''
注册验证
'''


@csrf_exempt
def register_now(request):
    vercode = None  # 邮箱密钥对象
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get('email')
    get_vercode = request.POST.get("vercode")
    # 防止用户恶意提交长数据
    if len(username) > 50 or len(password) > 50 or len(get_vercode) > 10:
        msg = '提交的信息过长，被后端拦截'
        return HttpResponse(msg)

    try:
        get_user_by_username(username)
        msg = '用户名已存在'
        return HttpResponse(msg)
    except:
        pass

    if re.match(password_safe, password):
        pass
    else:
        msg = '密码请包含大写字母、小写字母、特殊符号、数字中的任意三项'
        return HttpResponse(msg)

    try:
        vercode = get_vercode_by_username(username)
    except:
        pass
    now_time = datetime.now()
    str_d1 = now_time.strftime('%Y-%m-%d %H:%M:%S')
    str_d2 = vercode.last_modified.strftime('%Y-%m-%d %H:%M:%S')
    date_d1 = datetime.strptime(str_d1, '%Y-%m-%d %H:%M:%S')
    date_d2 = datetime.strptime(str_d2, '%Y-%m-%d %H:%M:%S')
    d = (date_d1 - date_d2).seconds
    if vercode.code != get_vercode:
        msg = '邮箱密钥错误'
        return HttpResponse(msg)
    if d > 520:
        msg = '邮箱密钥错误'
        return HttpResponse(msg)
    else:
        # 在数据库中新增用户
        add_user(username, password, email)
        user = login_blocking(username, password)
        # 用户注册后直接进行登录
        login(request, user)
        # 记录用户的IP信息
        user_ip = request.META.get('REMOTE_ADDR')
        try:
            user = get_user_by_username(username)
        except:
            pass
        add_ipUID_userinfo(user_ip, user)
        return HttpResponse('ok')
