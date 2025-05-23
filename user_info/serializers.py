# user_info/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UserDescSerializer(serializers.ModelSerializer):
    """于文章列表中引用的嵌套序列化器"""
    class Meta:
        model = User # 指定这个类操作的是哪一个模型
        fields = [
            'id',
            'username',
            'last_login',
            'date_joined'
        ]