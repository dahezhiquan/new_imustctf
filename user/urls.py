from django.urls import path
from .views import *
from .send_email import *
from .login_register import *

urlpatterns = [
    path('login/', login_),
    path('register/', register_),
    path('get_login_key/', get_email_key),
    path('get_register_key/', get_email_username_key),
    path('login_now/', login_now),
    path('register_now/', register_now),
    path('logout/', logout_),
]
