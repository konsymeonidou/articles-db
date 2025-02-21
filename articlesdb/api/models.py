from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    publication_date = models.DateField()
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    # authors = models.JSONField(default=list)  # Store authors as a list
    authors = models.ManyToManyField(User)
    tags = models.JSONField(default=list)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment by {self.created_by} on {self.article.title}"
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
