from django.contrib import admin
from .models import Article

# 登录admin后台后可以编辑article
admin.site.register(Article)
