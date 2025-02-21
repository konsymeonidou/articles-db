from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Tag, Comment
from .views import ArticleViewSet, TagViewSet, CommentViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# add more tests here

class TestModels(TestCase):
    def setUp(self):
        self.author = User.objects.create(username='test_user', password='test')
        self.tag = Tag.objects.create(name='test_tag')

    def test_model_article(self):    
        article_item = Article.objects.create(title='test_article', abstract='test_abstract')
        article_item.authors.add(self.author)
        article_item.tags.add(self.tag)
        article_item.save()
        self.assertEqual(str(article_item), 'test_article')
        self.assertTrue(isinstance(article_item, Article))

    def test_model_tag(self):
        Tag.objects.filter(name='test_tag').delete()
        tag_item = Tag.objects.create(name='test_tag')
        self.assertEqual(str(tag_item), 'test_tag') 
        self.assertTrue(isinstance(tag_item, Tag))

    def test_model_comment(self):
        article_item = Article.objects.create(title='test_article', abstract='test_abstract')
        article_item.authors.add(self.author)
        article_item.tags.add(self.tag)
        article_item.save()
        print(article_item)
        comment_item = Comment.objects.create(user=self.author, article=article_item, text='test_text')
        self.assertEqual(str(comment_item), 'Comment by test_user on test_article')
        self.assertTrue(isinstance(comment_item, Comment))
