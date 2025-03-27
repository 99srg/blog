from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

class TestApp(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        return super().setUp()

    def test_menu_calls_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
                app.menu()

                mocked_ask_create_blog.assert_called_with()

    def test_menu_calls_print_blogs_when_typed_l(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:
                mocked_input.side_effect = ('l', 'q')
                app.menu()

                mocked_print_blogs.assert_called_with()

    def test_menu_calls_read_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_ask_read_blog:
                mocked_input.side_effect = ('r', 'Test', 'Test Author', 'Test', 'q')
                app.menu()

                mocked_ask_read_blog.assert_called_with()

    def test_menu_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_input.side_effect = ('p', 'Test', 'Test Author', 'q')
                app.menu()

                mocked_ask_create_post.assert_called_with()

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value = 'q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value = "q"):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print: # this is a context manager
            app.print_blogs()
            mocked_print.assert_called_with('- <The blog Test written by the author Test Author has 0 posts>')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value = 'Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        
        post = Post('Post Title', 'Post Content')
        expected_print = '''
--- Post Title ---

Post Content

'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')