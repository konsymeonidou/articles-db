from django.shortcuts import render
from rest_framework import viewsets
from .models import Article, Comment, Tag
from .serializers import ArticleSerializer, CommentSerializer, TagSerializer
import csv
from django.http import HttpResponse
from rest_framework.decorators import action

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        authors = [self.request.user]  # Add the user who creates the article
        authors += serializer.validated_data.get('authors', [])  # Add the specified authors
        serializer.save(authors=authors)

    def list(self, request, *args, **kwargs):
        # Store the current filter parameters in the session
        request.session['article_filter_params'] = request.GET.urlencode() # urlencode method converts filter params to URL-encoded string
        print(request.session['article_filter_params'])
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def export_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="articles.csv"'

        writer = csv.writer(response)
        writer.writerow(['Identifier', 'Title', 'Publication Date', 'Authors', 'Abstract', 'Tags'])

        articles = self.get_queryset()
        for article in articles:
            writer.writerow([article.identifier, article.title, article.publication_date, article.authors, article.abstract, article.tags])

        return response

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        serializer.save()
