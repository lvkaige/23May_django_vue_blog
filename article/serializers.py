# articles/serializers.py
from rest_framework import serializers
from .models import Article
from user_info.serializers import UserDescSerializer
# 序列化：将后端存储的变量转换成json格式；逆序列化：将json转换成前端可以读取的格式


class ArticleListSerializer(serializers.ModelSerializer):
    # read_only 参数设置为只读
    author = UserDescSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="article:detail")

    class Meta:
        # 指定这个类操作的是哪一个模型
        model = Article
        fields = [
            # 'id',
            'url',
            'title',
            'created',
            'author',
        ]
        # 嵌套序列化器已经设置了只读，所以这个就不要了
        # read_only_fields = ['author']

# 文章的内容（点开文章之后）
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article # 指定这个类操作的是哪一个模型

        # __all__是指所有字段
        fields = '__all__'