'''
使用redis增加军火的点赞，下载，浏览，分享数
这里生产环境的redis要确保开启aof持久化
'''
import redis
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

'''
redis连接池
'''
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

'''
增加下载量
'''


@csrf_exempt
def add_download_count(request):
    armname = request.POST.get("armname")
    # 缓存中不存在该军火的hash值则添加一个新的军火对象缓存
    # 存在的话就将下载量 + 1
    if not r.hexists(armname, "download"):
        r.hmset(armname, {"likes": 0, "download": 1, "share": 0, "watch": 1})
    else:
        r.hincrby(armname, "download", amount=1)
        r.hincrby(armname, "watch", amount=1)

    return HttpResponse('ok')


'''
增加分享数量
'''


@csrf_exempt
def add_share_count(request):
    armname = request.POST.get("armname")
    # 缓存中不存在该军火的hash值则添加一个新的军火对象缓存
    # 存在的话就将分享量 + 1
    if not r.hexists(armname, "share"):
        r.hmset(armname, {"likes": 0, "download": 0, "share": 1, "watch": 1})
    else:
        r.hincrby(armname, "share", amount=1)
        r.hincrby(armname, "watch", amount=1)

    return HttpResponse('ok')


'''
增加喜欢数量
'''


@csrf_exempt
def add_like_count(request):
    armname = request.POST.get("armname")
    # 缓存中不存在该军火的hash值则添加一个新的军火对象缓存
    # 存在的话就将分享量 + 1
    if not r.hexists(armname, "likes"):
        r.hmset(armname, {"likes": 1, "download": 0, "share": 0, "watch": 1})
    else:
        r.hincrby(armname, "likes", amount=1)
        r.hincrby(armname, "watch", amount=1)

    return HttpResponse('ok')
