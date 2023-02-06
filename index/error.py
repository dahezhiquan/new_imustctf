'''
错误处理视图
'''
from django.shortcuts import render


# 404
def page_not_found(request, exception, template_name='error/404.html'):
    return render(request, template_name)


# 500
def server_error(request, template_name='error/500.html'):
    return render(request, template_name)
