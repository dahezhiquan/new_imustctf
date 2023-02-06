"""
IMUSTCTF项目的 WSGI 配置

它将 WSGI 可调用公开为名为“应用程序”的模块级变量

有关此文件的更多信息，请参阅
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IMUSTCTF.settings')

application = get_wsgi_application()
