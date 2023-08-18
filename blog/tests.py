from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

# Model Tests
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create(username='testuser')
        Post.objects.create(title='Test Post', author=user)

    def test_title_label(self):
        post = Post.objects.get(id=2)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        post = Post.objects.get(id=2)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create(username='testuser')
        post = Post.objects.create(title='Test Post', author=user)
        Comment.objects.create(post=post, name='Test Name', email='test@testuser.com', body='Test comment body')

    def test_name_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    def test_name_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('name').max_length
        self.assertEqual(max_length, 80)