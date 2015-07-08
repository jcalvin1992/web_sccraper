import collections
import datetime

import requests
from bs4 import BeautifulSoup as BS


from web_utilitys import EasyUrl#, HistoryManager



class BaseScraper(object):
	""" Prefroms basic http request calls using the requests library """
	
	def __init__(self, url):

		self.first_url = url 		# Don't change this variable.
		self.url = EasyUrl(url) 	# Our url variable that can be modified
		
		print '\n\n' + str(self.url) + '\n\n'

		self.soup = None			# A BeautifulSoup (BS) object of the last requests html source
		self.response = None		# The last response recieved after a request
		
		# An enhanced dictionary for tracking our scrapers tracks.
#		self.history = HistoryManager()

	def __len__(self):
		return len(self.response.text)


	def get(self, payload={}):
		#sent_timestamp = datetime.datetime.now()
		self.response = requests.get(self.url, params=payload)
		self.soup = BS(self.response.text)

		#self.history.Create(self.url, self.response, sent_timestamp)
		return self.response

	def get_by_new_url(self, url, payload={}):
		self.url = url
		return self.get(payload)


	def post(self, payload={}):
		self.response = requests.post(self.url, payload)
		self.soup = BS(self.response.text)
		return self.response
		
	def post_by_new_url(self, url, payload={}):
		self.url = url
		return self.post(payload)




url  = 'thehackernews.com'
s1 = BaseScraper(url)
response = s1.get()


print response == s1.response
print hex(id(response))
print hex(id(s1.response))
print id(response) == id(s1.response)
print s1.soup.title



