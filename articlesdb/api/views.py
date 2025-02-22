from rest_framework import viewsets, filters
from .models import Article, Comment, Tag
from .serializers import ArticleSerializer, CommentSerializer, TagSerializer
import csv
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = PageNumberPagination 

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'publication_date': ['year', 'month'],
        'authors__name': ['exact'],
        'tags__name': ['exact'],
    }
    search_fields = ['title', 'abstract']


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
    permission_classes  = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        serializer.save()
