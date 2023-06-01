from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from .models import Category, Tag, Post, Comment, Rating


def post_list_detail(request, slug=None):
    if slug:
        post = get_object_or_404(Post, slug=slug, published='pub')
        return render(request, 'blog/post_detail.html', {'post': post})
    else:
        posts = Post.objects.filter(published='pub').order_by('-created_at')
        return render(request, 'blog/post_list.html', {'posts': posts})
