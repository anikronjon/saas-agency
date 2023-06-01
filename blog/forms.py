from django import forms
from .models import Category, Tag, Post, Comment, Rating


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'parent')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'published', 'categories', 'tags')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('value',)


