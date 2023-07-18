# 分类
from django.db import connection

from django.db.models import Count

from .models import *


def getRightInfo(request):
    r_admin_post = AdminUser.objects.all()[0]  # 标签
    # r_announcement_post = adminUser.objects.values('announcement')  # 公告
    r_tag_post = Post.objects.values('tag__tname').annotate(c=Count('*'))  # 标签
    r_cate_post = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')  # 分类
    # print(r_cate_post)
    r_recent_post = Post.objects.order_by('-created')[:4]  # 排序取前五，近期文章

    cursor = connection.cursor()
    filepost = cursor.execute(
        'select created,count("*") count from t_post GROUP by strftime("%Y-%m",created) order by count desc'
        # 查询t_post表，并按照年月(created字段)进行分组归档，统计每个月份的帖子数量
    )  # 归档，sql语句
    r_file_post = filepost.fetchall()  # 获取结果,[(datetime.datetime(2023, 7, 15, 22, 52, 11, 503352), 11)]
    return {'r_admin_post':r_admin_post,'r_tag_post': r_tag_post, 'r_cate_post': r_cate_post,
            'r_recent_post': r_recent_post, 'r_file_post': r_file_post}
