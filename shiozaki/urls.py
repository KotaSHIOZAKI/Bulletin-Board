from django.contrib import admin
from django.urls import path
from . import views

#config/urls.pyにて、path('', include('shiozaki.urls')),を追加
urlpatterns = [
    path('', views.ShiozakiView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
    path('board-list/', views.BoardListView.as_view(), name='board-list'),
    path('board-detail/', views.BoardDetailView.as_view(), name='board-detail'),
]
