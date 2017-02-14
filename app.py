import pprint

from database import Database
from models.blog import Blog

lineBreak = '***'
__author__ = 'Craig Ballingall'

Database.initdb()

blog = Blog(author='Craig Ballingall',
            title='England Rugby are the BOMB!',
            description='Some stuff about england being cool')

blog.new_post()

blog.savedb()

from_database = Blog.from_mongo(blog.id)

pprint.pprint(blog.get_post())








