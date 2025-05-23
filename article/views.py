from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from article.serializers import ArticleListSerializer
from django.http import JsonResponse

# 较基础的方法
# def article_list(request):
#     articles = Article.objects.all()
#     serializer = ArticleListSerializer(articles, many=True)
#     return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
def article_list(request):
    # 同一个函数的不同请求方式
    if request.method == 'GET':
        articles = Article.objects.all()
        # 使用定义的序列化方法把文章列表数据序列化一下，将数据库中读取的数据转换成json格式
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)

        # 数据合法的话就保存了
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # 不合法就反馈错误
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return None