from django.shortcuts import render
from .models import Article
from article.serializers import ArticleListSerializer
from django.http import JsonResponse

def article_list(request):
    articles = Article.objects.all()

    # 使用定义的序列化方法把文章列表数据序列化一下，将数据库中读取的数据转换成json格式
    serializer = ArticleListSerializer(articles, many=True)

    return JsonResponse(serializer.data, safe=False)