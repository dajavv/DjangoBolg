from __future__ import unicode_literals
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)  # 注册到admin控制面板中
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(AdminUser)