from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, toggle_publish

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_item'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/toggle/<int:pk>/', toggle_publish, name='toggle_publish')
]