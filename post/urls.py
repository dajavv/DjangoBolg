from django.contrib import admin
from django.urls import path, include
from post import views  # 导入views
from post.views import IndexViex, DetailViex, getPostByCid

urlpatterns = [
    path('', IndexViex.as_view(), name='主页'),
    path('page/<int:num>/', views.IndexViex.as_view(), name='页面'), #路由配置
    path('post/<int:postid>/', views.DetailViex.as_view(), name='文章'), #路由配置
    path('category/<int:category>/', views.getPostByCid, name='分类'), #路由配置
    path('tags/<str:tag>/', views.getPostTags, name='标签'), #路由配置
    path('archives/', views.getPostArchives, name='归档'), #路由配置
    path('about/', views.About, name='关于'), #路由配置
]
