from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Tag, Comment, Author
from datetime import date

# add more tests here

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', password='test')
        self.author = Author.objects.create(name='test_author')
        self.tag = Tag.objects.create(name='test_tag')

        self.article = Article.objects.create(
            identifier="12345",
            publication_date=date.today(),
            abstract="This is an abstract.",
            title="Sample Article"
        )
        self.article.authors.add(self.author)
        self.article.tags.add(self.tag)

    def test_model_article(self):    
        article_item=self.article
        article_item.save()
        self.assertEqual(str(article_item), 'Sample Article')
        self.assertTrue(isinstance(article_item, Article))

    def test_model_tag(self):
        Tag.objects.filter(name='test_tag').delete()
        tag_item = Tag.objects.create(name='test_tag')
        self.assertEqual(str(tag_item), 'test_tag') 
        self.assertTrue(isinstance(tag_item, Tag))

    def test_model_comment(self):
        article_item = self.article
        article_item.save()
        print(article_item)
        comment_item = Comment.objects.create(user=self.user, article=article_item, text='test_text')
        self.assertEqual(str(comment_item), 'Comment by test_user on Sample Article')
        self.assertTrue(isinstance(comment_item, Comment))
