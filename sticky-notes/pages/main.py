__author__ = 'Lucian Tuca'

import webapp2

from google.appengine.api import users


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.redirect('/notes')
        else:
            self.redirect(users.create_login_url(self.request.uri))