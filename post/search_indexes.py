from haystack import indexes
from post.models import *


# 注意格式(模型类名+Index )
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)  # 打开搜索
    # 给titlejcontent设置索引
    title = indexes.NgramField(model_attr='title ')  # 根据字段搜索
    content = indexes.NgramField(model_attr='content ')

    def get_model(self):
        return Post  # 返回模型类

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')  # 搜索并排序，根据创建时间排序
