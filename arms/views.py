from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

'''
军火库主页
'''


@login_required(redirect_field_name='arms_index')
def arms_index(request, type, model_type):
    search_data = ''
    if request.GET.get("search_data") != None:
        search_data = request.GET.get("search_data")
    arms = get_arms(type, model_type, 1, search_data)
    for arm in arms:
        labels = arm.label.split(';')
        arm.label = labels
    return render(request, "arms_index.html", {"arms": arms, "type": type})
