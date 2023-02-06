from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User

'''
用户个人信息表
'''


class Info(models.Model):
    name = models.CharField(max_length=255, help_text=u'姓名')
    UID = models.ForeignKey(to=User, to_field='id', on_delete=models.CASCADE, help_text=u'用户UID')
    specialty = models.CharField(max_length=255, help_text=u'专业')
    studentID = models.CharField(max_length=255, help_text=u'学号')
    self_introduction = models.TextField(max_length=500, help_text=u'自我介绍')
    ip = models.CharField(max_length=255, help_text=u'IP地址')
    hobby = models.CharField(max_length=255, help_text=u'爱好的CTF项目')

    def __str__(self):
        return '%d:%s' % (self.id, self.name[0:20])


'''
验证码分发记录表
'''


class Vercode(models.Model):
    username = models.CharField(max_length=255, help_text=u'用户名', default='error')
    code = models.CharField(max_length=255, help_text=u'验证码')
    last_modified = models.DateTimeField(auto_now=True, help_text=u'上次分发时间')

    def __str__(self):
        return '%d:%s' % (self.id, self.username[0:20])


# 通过邮箱号获取用户对象
def get_user_by_email(email):
    return User.objects.get(email=email)


# 通过用户名获取用户对象
def get_user_by_username(username):
    return User.objects.get(username=username)


# 新增vercode行，不存在创建，存在则更新
def add_vercode(username, code):
    Vercode.objects.update_or_create(username=username, defaults={"code": code})


# 登录认证
def login_blocking(username, password):
    return auth.authenticate(username=username, password=password)


# 通过用户名获取验证密钥
def get_vercode_by_username(username):
    return Vercode.objects.get(username=username)


# 用户表中新增用户
def add_user(username, password, email):
    User.objects.create_user(username=username, password=password, email=email)


# info表中新增用户ip和UID信息
def add_ipUID_userinfo(user_ip, user):
    info = Info(ip=user_ip, UID=user)
    info.save()


# 查询IMUSTCTF注册人数
def get_imustctfer_cnt():
    return User.objects.all().count()
