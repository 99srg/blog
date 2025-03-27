from unittest import TestCase
from blog import Blog

class TestBlog(TestCase):

    def test_create_post(self):
        b = Blog('MyBlog', 'Sergio')
        b.create_post('My first post', 'Hello, this is my first post.')
        b.create_post('My second post', "Hello, this is my second post")

        self.assertEqual(b.posts[0].title, 'My first post')
        self.assertEqual(b.posts[0].content, 'Hello, this is my first post.')
        self.assertEqual(len(b.posts), 2)

    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')
        expected = {'title': 'Test', 'author': 'Test Author', 'posts': []}

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {'title': 'Test Post',
                 'content': 'Test Content'}
            ]
            }

        self.assertDictEqual(expected, b.json())    