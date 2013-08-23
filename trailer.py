import webapp2
import urllib2
import json
from random import choice
	
LIST_OF_VIDEOS = []

def get_embed_code(url):
        return "<p><h2>View today's popular trailers on YouTube</h2></p><object height=\"390\" width=\"640\"><param name=\"movie\" value=\"" + url + "&autoplay=1&loop=0\" /><embed height=\"390\" src=\"" + url + "&autoplay=1&loop=0\" type=\"application/x-shockwave-flash\" width=\"640\"></embed></object>"
	
def embed_button():
	return "<br><form action=\"/next\"><input type=\"submit\" value=\"Next Random Trailer\"></form><br><br><br><p>Created by <a href=\"http://www.goel.im\">Karan Goel</a>. [<a href=\"https://github.com/thekarangoel/popular-trailers\">Source</a>]</p>"

class MainPage(webapp2.RequestHandler):
	def get(self):
                self.response.write('<p>' + get_embed_code(choice(LIST_OF_VIDEOS)) + '</p>')
		self.response.write(embed_button())
		
def get_all_videos():
		url = "http://gdata.youtube.com/feeds/api/videos?vq=trailer&category=Film&racy=include&orderby=viewCount&time=today&v=2&alt=jsonc"
		response = urllib2.urlopen(url)
		json_obj = json.loads(response.read())
		for video in json_obj['data']['items']:
			LIST_OF_VIDEOS.append(video['content']['5'])
				
get_all_videos()
application = webapp2.WSGIApplication([('/', MainPage), ('/next', MainPage), ], debug=True)
