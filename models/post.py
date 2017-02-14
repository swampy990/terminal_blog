import uuid
import datetime

from database import Database

__author__ = 'Craig'

class Post(object):
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blogID = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        self.created_date = date

    def savedb(self):
        Database.insert(collection ='posts', data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blogID': self.blogID,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(id):
        post_data =  Database.find_one(collection='posts', query={'id': id})
        return cls(blogid=post_data['blogid'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['date'],
                   blgid=post_data['blgid'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blogID': id})]


