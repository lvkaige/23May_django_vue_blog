from django.urls import path,include
from . import views

urlpatterns = [
    # path('', views.article_list, name='article_list'),
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'), # 文章详情的url，为什么加上了一个as_view(),是因为views中，ArticleDetail是一个类，并不是函数，as_view是用来处理类class的
]
