import collections
import time, email, urlparse

class EasyUrl(object):
	""" A string object that has a url parts accessable through attributes. """
	def __init__(self, url):
		self.url = url
		
		print 'Inside EasyUrl __init__'

		self.urlparsed_url = urlparse.urlparse(url)

		print 'Passed urlparsed_url'
		print repr(self.urlparsed_url.scheme)

		self.scheme = ''
		self.host = ''
		self.path = ''
		self.spath = []		# path split by slashes
		self.params = {}	# dictionary for parameters passed through url
		self.fragmentclae = ''	# the urls fragment

		self.find_url_parts()
		self.fix_url_parts()


	def __str__(self):
		return self.url

	def __repr__(self):	return self.__str__()


	def find_url_parts(self):
		self.find_scheme()		# sets self.scheme to the url's scheme
		self.find_host()		# sets self.host to the url's hostname (netloc) 
		self.find_path()		# sets self.path to the url's path and self.spath to the split version the path
		self.find_params()		# sets self.params to the url's public arguments (query)
		self.find_fragment()	# sets the self.fragment if there is one.

	def find_scheme(self):
		self.scheme = self.urlparsed_url.scheme
	def find_host(self):
		self.host = self.urlparsed_url.netloc
	def find_path(self):
		self.path = self.urlparsed_url.path
	def find_params(self):
		self.params = self.urlparsed_url.params
	def find_fragment(self):
		self.fragment = self.urlparsed_url.fragment


	def fix_url_parts(self):
		# if no scheme exists add one, or expect an error(exception) from the requests library
		print 'inside fix-url-parts'
		if self.scheme is '':
			print 'inside if-statment'
			self.scheme = 'http://'
		print self.scheme
		print 'leaving fix-url-parts'

		self.url = self.scheme + self.host + self.path + self.params + self.fragment




