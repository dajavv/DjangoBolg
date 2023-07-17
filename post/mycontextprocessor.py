# 分类
from django.db.models import Count

from .models import *


def getRightInfo(request):
    # r_announcement_post = adminUser.objects.values('announcement')  # 公告
    r_tag_post = Post.objects.values('tag__tname').annotate(c=Count('*'))  # 标签
    r_cate_post = Post.objects.values('category__cname').annotate(c=Count('*')).order_by('-c')  # 分类

    r_recent_post = Post.objects.order_by('-created')[:4]  # 排序取前五，近期文章

    return {'r_tag_post': r_tag_post, 'r_cate_post': r_cate_post,
            'r_recent_post': r_recent_post}
