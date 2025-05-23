from rest_framework import serializers
from .models import Article
# 序列化：将后端存储的变量转换成json格式；逆序列化：将json转换成前端可以读取的格式


# 基础定义序列化文章列表的方法
# class ArticleListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(allow_blank=True, max_length=100)
#     body = serializers.CharField(allow_blank=True)
#     created = serializers.DateTimeField()
#     updated = serializers.DateTimeField()

# 更常用的方法，父类变成了 ModelSerializer
# 文章列表，未点开文章时候
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
        ]


# 文章的内容（点开文章之后）
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        # __all__是指所有字段
        fields = '__all__'