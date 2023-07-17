from django.db import models


# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name=u'类别名称')

    def __unicode__(self):
        return u'<Category:%s>' % self.cname

    class Meta:
        db_table = 't_category'  # 表名
        verbose_name_plural = u'类别'


class Tag(models.Model):
    tname = models.CharField(max_length=20, unique=True, verbose_name=u'标签')

    def __unicode__(self):
        return u'<Tag:%s>' % self.tname

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = u'标签'


from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name=u'标题')
    desc = models.CharField(max_length=200, verbose_name=u'简介')
    content = RichTextUploadingField(null=True, blank=True, verbose_name=u'内容')  # 引入控件
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'发帖时间')  # 当前时间
    modified = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')  #
    isdelete = models.BooleanField(default=False, verbose_name=u'是否删除')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=u'所属类别')
    tag = models.ManyToManyField(Tag, verbose_name=u'所属标签')
    words = models.CharField(max_length=15, verbose_name=u'字数')
    photos = models.CharField(max_length=300, verbose_name=u'封面图片')

    def __unicode__(self):
        return u'<Post:%s>' % self.title

    class Meta:
        db_table = 't_Post'
        verbose_name_plural = u'帖子'


# class AdminUser(models.Model):
#     aname = models.CharField(max_length=20, unique=True, verbose_name='名字')
#     avatar = models.CharField(max_length=200, unique=True, verbose_name='头像')
#     signature = models.CharField(max_length=100, unique=True, verbose_name='签名')
#     announcement = models.CharField(max_length=200, unique=True, verbose_name='公告')
#
#     def __unicode__(self):
#         return u'<AdminUser:%s>' % self.aname
#
#     class Meta:
#         db_table = 't_AdminUser'
#         verbose_name_plural = u'管理用户信息'
