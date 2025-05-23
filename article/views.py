from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse, Http404
from article.serializers import ArticleListSerializer, ArticleDetailSerializer
# from rest_framework.permissions import IsAdminUser
from article.permissions import IsAdminUserOrReadOnly

from .models import Article


class ArticleListView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]  # 判断权限，权限信息在permissions.py里面

    # 创建article时候，加上作者信息
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            self.perform_create(serializer) # 保存文章的时候，自动加上作者
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 用类的方式来写函数
# noinspection PyMethodMayBeStatic
class ArticleDetail(APIView):
    permission_classes = [IsAdminUserOrReadOnly]
    # 这是一个普通的函数，获取某特定id的article
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except:
            raise Http404

    # 这里的get,put,delete并不是简单的函数，他们指的是request.method,即GET请求、PUT请求、DELETE请求
    def get(self, request, pk):
        article = self.get_object(pk)
        # 将从数据库找到的数据序列化，以json形式返回给前端
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    # 修改article内容
    def put(self, request, pk):
        article = self.get_object(pk)
        # 接收到数据，反序列化
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid():
            # 数据合法的话，就保存到数据库
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 删除article
    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        # 删除成功后返回204
        return Response(status=status.HTTP_204_NO_CONTENT)


