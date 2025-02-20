from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    publication_date = models.DateField()
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    authors = models.JSONField(default=list)  # Store authors as a list
    tags = models.JSONField(default=list)  # Store tags as a list

    def __str__(self):
        return self.title

class Comment(models.Model):
    # user = models.ForeignKey(User)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_by = models.CharField(max_length=100)  # Store the user who created the comment
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.created_by} on {self.article.title}"
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
