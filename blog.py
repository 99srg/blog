from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self) -> str:
       # return f"<The blog {self.title} written by the author {self.author} has {len(self.posts)} posts>"
        return "<The blog {} written by the author {} has {} post{}>".format(self.title,
                                                                             self.author,
                                                                             len(self.posts),
                                                                             's' if len(self.posts) != 1 else '')
    
    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }
    
    def create_post(self, title, content):
        self.posts.append(Post(title, content))
