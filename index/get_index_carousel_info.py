'''
接口
'''
import json
import requests
from IMUSTCTF import settings

'''
获取首页轮播热榜
IT之家每日热榜接口
'''


def get_hotlist():
    key = settings.QQ_API_KEY  # API-Key
    type = "itzhijia"  # 平台类型

    url = 'https://qqlykm.cn/api/hotlist/get?key=' + key + '&type=' + type
    # 防止API响应发生异常
    try:
        return_data = requests.get(url)
    except:
        return None

    if return_data.status_code != 200:
        return None
    else:
        hot_dict = json.loads(return_data.text)
        # 只获取前三条热榜信息
        needs_hot_data = hot_dict['data'][0:3]

    return needs_hot_data


'''
获取首页轮播图片
必应每日图片接口
'''


def get_pic():
    format = "js"  # json格式输出
    idx = '0'  # 表示今日的壁纸
    n = '3'  # 需要的图片张数

    url = 'http://cn.bing.com/HPImageArchive.aspx?format=' + format + '&idx=' + idx + '&n=' + n
    needs_pic_data = []
    # 防止API响应发生异常
    try:
        return_data = requests.get(url)
    except:
        return None

    if return_data.status_code != 200:
        return None
    else:
        pic_dict = json.loads(return_data.text)
        pic_list = pic_dict['images']
        for pic in pic_list:
            needs_pic_data.append('https://www.bing.com' + pic['url'])

    return needs_pic_data


'''
获取首页宣传视频
bilibili视频解析接口
'''

def get_bilibili_video():
    key = settings.QQ_API_KEY  # API-Key
    id = "BV1VW411f74S"  # BV号

    url = 'https://qqlykm.cn/api/bilibili/get?key=' + key + '&id=' + id
    # 防止API响应发生异常
    try:
        return_data = requests.get(url)
    except:
        return None

    if return_data.status_code != 200:
        return None
    else:
        video_dict = json.loads(return_data.text)
        needs_video_data = video_dict['data']

    return needs_video_data

