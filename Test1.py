import os 
import json
import urlib
import webapp2

from google.appengine.ext.webapp,import template

class MainPage(webapp2.RequestHandler):
     def get(self):
     template_values ={}
     path=os.path.json(os.path.dirname(_file_),'index.html')
     self.response.out.write(templa