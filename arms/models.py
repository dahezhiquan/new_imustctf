import redis
from django.db import models
from django.db.models import Q

'''
redis连接池
'''
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

'''
军火表
'''

# 每页元素个数
PAGE_SIZE = 21


class Arms(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text=u'军火名称')
    introduction = models.CharField(max_length=255, help_text=u'简介')
    label = models.CharField(max_length=255, help_text=u'标签【用分号隔开】')
    details = models.TextField(max_length=500, help_text=u'详情')
    type = models.CharField(max_length=255, help_text=u'类型')
    created_time = models.DateTimeField(auto_now_add=True, help_text=u'创建时间')
    img_src = models.TextField(max_length=2000, help_text=u'图片链接')
    download_src = models.TextField(max_length=2000, help_text=u'下载链接')
    watch = models.IntegerField(default=0, help_text=u'浏览数')

    def __str__(self):
        return '%d:%s' % (self.id, self.details[0:20])


'''
查询要显示在页面的军火数据
需要传入类型，页码，模糊搜索关键字，最新还是最热
'''


def get_arms(type, model_type, page, search_data):
    # 计算当前页码开始的元素序号
    begin = (page - 1) * PAGE_SIZE

    # 首先判断是不是传入的模糊搜索的值，如果是模糊搜索，则不需要指定type过滤
    if type == "all":
        if model_type == "new":
            arms = Arms.objects.filter(Q(name__contains=search_data)) \
                       .order_by('-created_time')[begin:begin + PAGE_SIZE]
        else:
            arms = Arms.objects.filter(Q(name__contains=search_data)) \
                       .order_by('-watch')[begin:begin + PAGE_SIZE]
        # 在model层对数据进行封装，将redis中的数据从内存中取出，添加到arms对象中
        for arm in arms:
            # redis缓存中不存在该arm对象的数据，则设置全0
            if not r.hexists(arm.name, "watch"):
                arm.count_data = {"likes": 0, "download": 0, "share": 0, "watch": 0}
            else:
                arm.count_data = r.hgetall(arm.name)
        return arms

    # 获取最新数据
    if model_type == "new":
        arms = Arms.objects.filter(Q(name__contains=search_data), type=type) \
                   .order_by('-created_time')[begin:begin + PAGE_SIZE]
        # 在model层对数据进行封装，将redis中的数据从内存中取出，添加到arms对象中
        for arm in arms:
            # redis缓存中不存在该arm对象的数据，则设置全0
            if not r.hexists(arm.name, "watch"):
                arm.count_data = {"likes": 0, "download": 0, "share": 0, "watch": 0}
            else:
                arm.count_data = r.hgetall(arm.name)
        return arms

    # 获取最热数据
    if model_type == "hot":
        # 意味着需要进行同步
        if r.get('is_update_watch') == None:
            synchronize_watch_from_redis()

        arms = Arms.objects.filter(Q(name__contains=search_data), type=type) \
                   .order_by('-watch')[begin:begin + PAGE_SIZE]
        # 在model层对数据进行封装，将redis中的数据从内存中取出，添加到arms对象中
        for arm in arms:
            # redis缓存中不存在该arm对象的数据，则设置全0
            if not r.hexists(arm.name, "watch"):
                arm.count_data = {"likes": 0, "download": 0, "share": 0, "watch": 0}
            else:
                arm.count_data = r.hgetall(arm.name)

        return arms


'''
从redis中取出watch字段的值同步在Mysql数据库对应的字段中
设置一个新的redis String值来记录是否需要同步，防止军火数量过大的时候同步数据库导致数据库崩溃
当记录值过期，也就是为None值的时候，意味着需要进行同步
'''


def synchronize_watch_from_redis():
    arms = Arms.objects.all()
    for arm in arms:
        if r.hexists(arm.name, "watch"):
            watch_count = r.hget(arm.name, "watch")
            Arms.objects.filter(name=arm.name).update(watch=watch_count)
    # 设置过期时间为3小时
    r.set('is_update_watch', 'yes', ex=10800)
