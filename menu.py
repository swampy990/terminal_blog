import pprint

from database import Database
from models.blog import Blog

__author__ = 'Craig Ballingall'

class Menu(object):
    def __init__(self):
        self.user = input("Please enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            pprint.pprint('Welcome Back')
        else:
            self._prompt_user_for_account()

        # ask user for author name
        # check if they already have an account
        # if not, prompt them to create one
        pass

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False


    def _prompt_user_for_account(self):
        title = input("Enter Blog Title: ")
        description = input("Enter Blog Description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.savedb()
        self.user_blog = blog


    def run_menu(self):
        # User read or write blobs?
        # if read:
            # List blogs in database
            # allow user to pick a blog
            # display posts
        # if write:
            # check if user has a blog
            # if they do prompt to write a post
    read_or_write = input("do you want to read (R) or write (W) blogs?: ")
    if read_or_write == 'R':
        pass
    elif read_or_write == 'W':
        pass
    else:
        pprint.pprint('Invalid input detected... Exiting')



