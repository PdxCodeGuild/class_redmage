from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

class ChirpListView(ListView):
    model = Post
    template_name = 'home.html'

class ChirpDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post_detail.html'

class ChirpCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['body']

    def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)


class ChirpDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')