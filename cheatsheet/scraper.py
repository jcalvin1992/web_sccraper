#!/usr/bin/python
from handles import StackOverFlow_HomeQuestions_Handle
from parser import ParsingHandle, ParsingManager
from web_utilities import parse_url, EasyUrl, HistoryEntry, HistoryManager 

import requests
from bs4 import BeautifulSoup as BS




class BaseScraper(object):
    """ Basic Framework of a simple web communication tool. """
   
    def __init__(self, url):
        self.set_url(url)
        self.response = None
        self.soup = None
        self.parser = ParsingManager()
        self.history = HistoryManager()
    
    # Getters / Setters/ Loaders
    def set_url(self, url):
        if type(url) is str:
            self.url = parse_url(url) # Returns a EasyUrl() object
        else:
            self.url = parse_url(str(url))
        
    def get_status_code(self):
        """ return self.response.status_code, the status of the last made request. """
        if self.response:
            return self.response.status_code
        else:
            return None
    
    def load_soup(self):
        """ creates a soup object from self.response. """
        if self.response:
            self.soup = BS(self.response.text)    


    # Web Communication Methods
    def get(self, payload={}):
        self.response = requests.get(self.url, params=payload)
        self.load_soup()
        self.history.save(self) # Save the state of the passed scraper
        
    
    
  
  
  
def stackoverflow_test():
    # Create a scraper
    url = 'http://stackoverflow.com/'
    scraper = BaseScraper(url)

    print '\nScraper Created:\n\tURL: %s' % str(scraper.url)    
    
    # Add some handles
    scraper.parser.add_handle(StackOverFlow_HomeQuestions_Handle())

    print '\nParsing Handles Added\n\n'
    
    print 'Making a get request...'

    # Make requests
    scraper.get()
    
    print 'Done\nResults:'
    print '\tStatus Code: %r' % scraper.response.status_code

    print '\nCalling \'Home Questions\' parsing handle\n\n'
    # #xtract data from request using our handles
    # Home Questions = the name of StackOverFlow_HomeQuestions_Handle()
    
    stackoverflow_questions = scraper.parser.call_handle_by_name(
        'Home Questions', scraper.soup
    ) 
    
#
#print 'Scraped %d questions from the home page.\n' % len(stackoverflow_questions)

    for question in stackoverflow_questions:
        print unicode(question)
        
    
    print 'There are %d questions scraped.' % len(stackoverflow_questions)




if __name__ == '__main__':
    stackoverflow_test()


