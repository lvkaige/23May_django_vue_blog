from rest_framework import serializers
from .models import Article
from user_info.serializers import UserDescSerializer
# 序列化：将后端存储的变量转换成json格式；逆序列化：将json转换成前端可以读取的格式

# 更常用的方法，父类变成了 ModelSerializer
# 文章列表，未点开文章时候
# class ArticleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = [
#             'id',
#             'title',
#             'created',
#             'author', # 作者信息
#         ]
#         read_only_fields = ['author']



class ArticleListSerializer(serializers.ModelSerializer):
    # read_only 参数设置为只读
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
            'author',
        ]
        # 嵌套序列化器已经设置了只读，所以这个就不要了
        # read_only_fields = ['author']

# 文章的内容（点开文章之后）
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        # __all__是指所有字段
        fields = '__all__'