from django.urls import path
from .views import *
from .add_count import *

urlpatterns = [
    path('index/<str:type>/<str:model_type>/', arms_index),
    path('index/add_download/', add_download_count),
    path('index/add_share/', add_share_count),
    path('index/add_like/', add_like_count),
]
