from django.shortcuts import render, reverse, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy, reverse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from django.views.generic import (
    ListView, 
    CreateView, 
    DetailView,
    UpdateView,
    DeleteView
)

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_posted']


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

class BlogUserView(LoginRequiredMixin, ListView):
    # model = Post
    template_name = "post_user.html"
    # ordering = ['-date_posted']
    context_object_name = "posts"

    def get_queryset(self):
        self.author = get_list_or_404(Post, author__username=self.kwargs['author'])
        
        return Post.objects.filter(author__username=self.kwargs['author']).order_by('-date_posted')


class BlogEditView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title', 'body']
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = "post"
    template_name="post_delete.html"
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user