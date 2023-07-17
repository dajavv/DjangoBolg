import math

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View  # 导入

from post.models import Post


# Create your views here.
class IndexViex(View):
    def get(self, request, num=1):
        num = int(num)  # 转型

        postList = Post.objects.all().order_by('-created')  # 查询所有的帖子信息,按照发帖时间排序
        page_obj = Paginator(postList, 10)  # 创建分页器对象，每一页显示一条记录
        page_post = page_obj.page(num)  # 获取num页的数据

        begin = int(num - math.ceil(10.0 / 2))  # 页码num在数组中的相对位置
        # print(begin)  # [-4,-3,-2,-1,0,1,2,3,4] 页面的相对位置?
        if begin < 1:  # 当前位置在1(数组后半段)之前,
            begin = 1  # 将当前位置变为1
        end = begin + 9
        if end > page_obj.num_pages:
            end = page_obj.num_pages  # 获取页码总数(最大页码)
        if end < 10:  #
            begin = 1
        else:
            begin = end - 9
        page_list = range(begin, end + 1)  # 构造一个最大为10的数组,并且里面的数字随着页面num的增大而变换，
        return render(request, 'index.html', {'postList': page_post, 'page_list': page_list, 'currentNum': num})


class DetailViex(View):
    def get(self, request, postid):
        postid = int(postid)
        post_obj = Post.objects.get(id=postid)  # 条件查询id
        return render(request,'detail.html',{'post_obj':post_obj})
