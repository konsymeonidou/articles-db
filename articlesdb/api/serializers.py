from rest_framework import serializers
from .models import Article, Comment, Tag, Author
from django.contrib.auth.models import User,AnonymousUser


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ['id', 'article', 'text', 'user', 'created_at', 'updated_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'identifier', 'publication_date', 'authors', 'abstract', 'title', 'tags', 'comments']

    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        tags_data = validated_data.pop('tags')
        article = Article.objects.create(**validated_data)
        for author_data in authors_data:
            author, _ = Author.objects.get_or_create(**author_data)
            article.authors.add(author)
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            article.tags.add(tag)
        return article

