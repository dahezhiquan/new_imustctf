'''
邮件分发
'''
import re
import smtplib
import random
from .models import *
from email.mime.text import MIMEText
from email.utils import formataddr
from IMUSTCTF import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse

# 发件人邮箱账号
my_sender = settings.MY_SENDER
# 发件人邮箱密码
my_pass = settings.MY_PASS
# email正则匹配字符串
email_match = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'

'''
发送邮件
'''


def mail(username, my_user):
    try:
        code = create_code()
        # 邮件内容
        msg = MIMEText('【IMUSTCTF】您的验证码为：' + code + '，请勿将此验证码泄露，验证码有效期：520秒', 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["IMUSTCTF", my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr([username, my_user])
        # 邮件的主题
        msg['Subject'] = "IMUSTCTF验证码"

        # SMTP服务器配置
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.close()
    except Exception:
        server.close()

    return code


'''
产生随机验证码
'''


def create_code():
    vercode = ''
    for i in range(6):
        num = random.randint(0, 9)
        vercode += str(num)
    return vercode


'''
登录页面，接收email-key的请求
'''


@csrf_exempt
def get_email_key(request):
    msg = '已发送'  # 向ajax反馈的值
    username = request.POST.get("username")
    # 用户使用邮箱登录
    if re.match(email_match, username):
        try:
            user = get_user_by_email(username)
            code = mail(user.username, user.email)
            add_vercode(user.username, code)
        except:
            msg = '用户不存在，请注册'
    else:
        try:
            user = get_user_by_username(username)
            code = mail(user.username, user.email)
            add_vercode(user.username, code)
        except:
            msg = '用户不存在，请注册'

    return HttpResponse(msg)


'''
注册页面，接收email-username-key的请求
'''


@csrf_exempt
def get_email_username_key(request):
    msg = '已发送'  # 向ajax反馈的值
    username = request.POST.get("username")
    email = request.POST.get("email")
    try:
        get_user_by_email(email)
        msg = '邮箱已被注册'
        return HttpResponse(msg)
    except:
        pass
    try:
        get_user_by_username(username)
        msg = '用户名已存在'
    except:
        if re.match(email_match, email):
            code = mail(username, email)
            add_vercode(username, code)
        else:
            msg = '邮箱格式有误'

    return HttpResponse(msg)
