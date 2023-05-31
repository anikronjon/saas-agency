from django.db import models
from account.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=12, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Post(models.Model):
    class PublicationStatus(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'pub', 'Published'
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    published = models.CharField(max_length=5, choices=PublicationStatus.choices, default=PublicationStatus.DRAFT)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class Rating(models.Model):
    VALUE_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    value = models.IntegerField(choices=VALUE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} rated {self.post.title} with {self.value} stars"
