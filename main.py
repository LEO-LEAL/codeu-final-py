#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
import webapp2
import jinja2
import os

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        greeting = ('<a href="%s">Sign in or register</a>.' %
            users.create_login_url('/main'))
        self.response.write('<html><boby>%s</body></html>' % greeting)

class MainHandler(webapp2.RequestHandler): #aka Seach Page
    def get(self):
        #login info
        user = users.get_current_user()
        greeting = ('<a id = "user" >Welcome, %s!</a>' '<a href=%s> sign_out</a>' %
            (user.nickname(), users.create_logout_url('/')))
        self.response.write('<html><boby>%s</body></html>' % greeting)
        #login end
        template = jinja2_environment.get_template('templates/search_page.html')
        self.response.write(template.render())

#class SeachResults(ndb.Model):
    #pass

class SeachHandler(webapp2.RequestHandler):
    def get(self):
        #query = SeachResults.query()
        #search_data = query.fetch()
        #template_vars = {'results': search_data}
        template = jinja2_environment.get_template('templates/search_results.html')
        self.response.write(template.render())#template_vars))

app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/main', MainHandler),
    ('/seached', SeachHandler)
], debug=True)

jinja2_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))
