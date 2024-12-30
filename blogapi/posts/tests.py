from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        testuser1 = User.objects.create(
            username = 'testuser1', password = '1234'
        )

        testuser1.save()

        test_post = Post.objects.create(
            author = testuser1, title='post1', body='blog post body'
        )

        test_post.save()
    
    def test_blog_post(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        author = f'{post.author}'

        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'post1')

