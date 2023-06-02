from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Tag, Post, Like, Comment, Rating


def post_list_detail(request, slug=None):
    if slug:
        post = get_object_or_404(Post, slug=slug, published='pub')
        likes = post.likes.all()
        comments = post.comments.all()
        rating = post.ratings.all()
        return render(request, 'blog/post_detail.html', {'post': post, 'likes': likes, 'comments': comments, 'rating': rating})
    else:
        posts = Post.objects.filter(published='pub').order_by('-created_at')
        return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        # Check if the user has already liked the post
        liked = Like.objects.filter(user=request.user, content_object=post).exists()
        if liked:
            pass
        else:
            # Create a new Like object
            like = Like(user=request.user, content_object=post)
            like.save()


@login_required
def comment_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        comment = Comment(user=request.user, content_object=post, content=comment_content)
        comment.save()


@login_required
def rating_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        rating_value = request.POST.get('rating_value')
        if rating_value:
            rated = Rating.objects.filter(user=request.user, content_object=post).exists()
            if rated:
                pass
            else:
                rating = Rating(user=request.user, content_object=post, value=rating_value)
                rating.save()