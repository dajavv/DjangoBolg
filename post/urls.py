from django.contrib import admin
from django.urls import path, include
from post import views  # 导入views
from post.views import IndexViex, DetailViex

urlpatterns = [
    path('', IndexViex.as_view(), name='index'),
    path('page/<int:num>/', IndexViex.as_view(), name='index_page'), #路由配置
    path('post/<int:postid>/', DetailViex.as_view(), name='index_page'), #路由配置
]