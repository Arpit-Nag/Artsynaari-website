from django.urls import path
from . import views

app_name = 'blog'
urlpatterns=[
    path('list',views.PostListView,name='post_list'),
    path('post/<int:pk>',views.PostDetailView,name='post_detail'),
]
