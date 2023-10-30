from django.urls import path
# 현재 폴더에 있는 views.py를 사용할 수 있게 가져와!
from . import views

urlpatterns = [
    # URL 끝이 /blog/정수/ 일 때 PostDetail 클래스로 처리
    path('<int:pk>/', views.PostDetail.as_view()),

    # URL 끝이 /blog/ 일 때 PostList 클래스로 처리
    path('', views.PostList.as_view()),

    # path('<int:pk>/', views.single_post_page),
    # path('', views.index),
]
