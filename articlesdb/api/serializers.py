from rest_framework import serializers
from .models import Article, Comment, Tag
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        # Ensure that `authors` and `tags` are JSON-serializable
        if 'authors' in validated_data and not isinstance(validated_data['authors'], list):
            validated_data['authors'] = []  # Default to an empty list if invalid
        if 'tags' in validated_data and not isinstance(validated_data['tags'], list):
            validated_data['tags'] = []  # Default to an empty list if invalid

        # Create the article instance
        return Article.objects.create(**validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name'] 