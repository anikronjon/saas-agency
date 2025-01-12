from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Category, Tag, Post, Like, Comment, Rating
from .forms import CommentForm, RatingForm


def post_list(request):
    posts = Post.objects.filter(published='pub').order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


class PostDetailView(View):
    def get(self, request, slug=None):
        post = get_object_or_404(Post, slug=slug, published='pub')
        likes = post.likes.all()
        rating = post.ratings.all()
        comments = post.comments.all()
        form = CommentForm()

        return render(request, 'blog/post_detail.html',
                      {'post': post, 'likes': likes, 'rating': rating, 'comments': comments, 'form': form})

    @method_decorator(login_required(login_url='/account/signin/'))
    def post(self, request, slug=None):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.content_object = post
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)

        post = get_object_or_404(Post, slug=slug, published='pub')
        likes = post.likes.all()
        rating = post.ratings.all()
        comments = post.comments.all()

        return render(request, 'blog/post_detail.html',
                      {'post': post, 'likes': likes, 'rating': rating, 'comments': comments, 'form': form})

