# blog/urls.py
from django.urls import path

from .views import (
    BlogDeleteView,
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView
)

urlpatterns = [
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='post_delete'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'), #new
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #new
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path('', BlogListView.as_view(),name='home'),
]

