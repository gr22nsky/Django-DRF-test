from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListAPIView.as_view(), name='article_list'),
    path('<int:pk>/', views.ArticleDetailAPIView.as_view(), name='article_detail'),
    path('<int:article_pk>/comments/', views.CommentListAPIView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetailAPIView.as_view(), name='comment_detail'),
]
