from unittest import TestCase
from blog import Blog

class TestBlog(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        # self.assertEqual(0, len(b.posts)) another way to compare lists

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2= Blog('My Day', 'Rolf')

        self.assertEqual("<The blog Test written by the author Test Author has 0 posts>", b.__repr__())
        self.assertEqual("<The blog My Day written by the author Rolf has 0 posts>", b2.__repr__())

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['My First Blog']

        b2= Blog('My Day', 'Rolf')
        b2.posts = ['Post1', 'Post2']

        self.assertEqual("<The blog Test written by the author Test Author has 1 post>", b.__repr__())
        self.assertEqual("<The blog My Day written by the author Rolf has 2 posts>", b2.__repr__())