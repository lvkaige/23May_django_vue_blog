from rest_framework import serializers

# 序列化：将后端存储的变量转换成json格式；逆序列化：将json转换成前端可以读取的格式


# 序列化文章的方法
class ArticleListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=100)
    body = serializers.CharField(allow_blank=True)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()