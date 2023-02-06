from .get_index_carousel_info import *
from django.shortcuts import render
from user.models import *
from django.contrib.auth.decorators import login_required

'''
主页
'''


@login_required(redirect_field_name='index')
def index(request):
    user_count = get_imustctfer_cnt()
    needs_hot_data = get_hotlist()
    needs_pic_data = get_pic()
    needs_video_data = get_bilibili_video()
    return render(request, "index.html", {"needs_hot_data": needs_hot_data, "needs_pic_data": needs_pic_data,
                                          "needs_video_data": needs_video_data, "user_count": user_count})
