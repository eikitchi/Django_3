from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
# from django.urls import reverse_lazy, reverse

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_object(self, **kwargs):
        views = super().get_object()
        views.increase_view_count()
        return views


class PostCreateView(CreateView):
    model = Post
    fields = ('name', 'content', 'image', 'published')
    success_url = reverse_lazy('blog:post_list', )


class PostUpdateView(UpdateView):
    model = Post

    fields = ('name', 'content', 'image', 'published')
    success_url = reverse_lazy('blog:post_list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


def toggle_publish(pk):
    post_item = get_object_or_404(Post, pk=pk)
    if post_item.published:
        post_item.published = False
    else:
        post_item.published = True

    post_item.save()

    return redirect(reverse('blog:blog_item', args=[post_item.pk]))
