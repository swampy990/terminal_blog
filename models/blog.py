import uuid
import datetime

from database import Database
from models.post import Post

__author__ = 'craig'


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter Post Title: ")
        content = input("Enter Post Content: ")
        date = input("Enter Post date, or leave blank to use current date and time (format DDMMYYYY) : ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.id,
                    author=self.author,
                    title=title,
                    content=content,
                    date=date)
        post.savedb()

    def get_post(self):
        return Post.from_blog(self.id)

    def savedb(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})
        return cls(author=blog_data['author'],
                    title=blog_data['author'],
                    description=blog_data['description'],
                    id=blog_data['id'])
