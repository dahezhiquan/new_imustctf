from django.contrib import admin
from django.urls import include, path
from index import views as home
from index import error as error_

urlpatterns = [
    path('day01where1013/', admin.site.urls),  # 后台管理页面
    path('', home.index),  # 主页
    path('user/', include('user.urls')),
    path('arms/', include('arms.urls')),
]

# 错误处理
handler404 = error_.page_not_found
handler500 = error_.server_error
