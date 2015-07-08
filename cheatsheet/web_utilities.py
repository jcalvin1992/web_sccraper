import urlparse




def parse_url(url):
    """ 
    Parse a url into a ParseResult() object then evolve that ParseResult()
    instance into an EasyUrl() object, finally return the EasyUrl() instance.
    """
    url = urlparse.urlparse(url)
    #print url.__class__
    return EasyUrl.EvolveParseResult(url)




class EasyUrl(urlparse.ParseResult):
    """ 
    Don't change the url at all, instead create a new EasyUrl() object.
    Use the python builtin methods to make the ParseResult() object friendlier. 
    """
    
    def __init__(self, url): 
        self = parse_url(url) # returns a EasyUrl object
        self.initialize_attributes()

    # EasyUrl Methods
    def initialize_attributes(self):
        """ 
        When creating an EasyUrl() instance through the
        EvolveParseResult() method, the __init__() method is never
        called, therefore it makes since to place our initialize code
        into a seperate method that we can call from both __init__() and
        EvolveParseResult().
        """
        self.host = self.netloc
        self.url = self.geturl()

        self.set_scheme_if_non('https')
        
        # The file extensions we are watching for. Either load the extensions
        # from a text file, or create a seperate python file contain a list
        # supported file extensions
        self.listed_file_extensions = [ 
            '.jpg', '.bmp', '.png',
            '.mp3', '.mp4', '.flv', '.avi',
            '.zip', '.7z', '.tar', '.tar.gz', '.tar.bz', '.rar',
            '.exe', '.git', '.torrent',
        ]   
        # Type Boolean: True or False
        # Urls contain some useful information. Depending on the framework the 
        # website is built on, a url can contain information about paths and files.
        # This is a glimpse of the sites computer system. Pretty Useful!
        self.is_file_extension = None  # Does this path end as a file?
        #self.file_extension = self.check_for_file_extension()
           
           
           
           
    def set_scheme_if_non(self, scheme='http'):
        print self.scheme
        if not self.scheme:
            self.scheme = scheme
            self._set_url()





    def _set_url(self):
        """ Updates our self.url by seting it to self.geturl()."""        
        self.url = self.geturl()    
            
            
    # Required Methods for Third parties
    # - requests
    #   - the url passed when making request must be a string (or have the find method)
    def find(self, *args, **kwargs):
        return self.url.find(*args, **kwargs)


    # Builtin Methods: Overriding the python builtin methods
    def __str__(self):
        return self.url
    
    def __repr__(self):
        return self.url
        #        return '<EasyUrl: %s>' % self.url
    
    def __unicode__(self):
        return self.url

    # Static Methods: Call from class definition, not using an instance.
    # example: 
    # Good: EasyUrl.EvolveParseresult(...)
    #
    # Bad : url = EasyUrl()
    #     : url = url.EvolveParseresult(...)
    @staticmethod
    def EvolveParseResult(parseresult):
        """ url, response
        Take a formally (through urlparse.urlparse) constructed
        ParseResult() object and transform it into this EasyUrl() object.
        """
        parseresult.__class__ = EasyUrl # This turns the the class to EasyUrl()
        
        easy_url = parseresult
        easy_url.initialize_attributes()
        return easy_url
    
    

class HistoryEntry(object):
    """ Keeps a collapsed form of a scraper state."""
    
    def __init__(self, url, response):
        self.url = url
        self.response = response
    
    def load_to_scraper(self, scraper):
        """ 
        Delegate the parameters from this HistoryEntry()
        to a scraper that is passed in as an argument.
        """
        scraper.url = self.url
        scraper.response = self.response
        scraper.load_soup()
        return scraper


class HistoryManager(dict):
    """ Stores and manages HistoryEntry's from a scraper. """

    def __init__(self, *history_entries):
#        super(HistoryEntry, self).__init__()
        self.load_history_entries(*history_entries)

    
    def load_history_entries(self, *entries):
        """ 
        Using HistoryEntries passed through the method call,
        populatet request...
'stackoverflow.com' the dictionary. The key being the site name, the
        value is a list containing all HistoryEntry's for that site.
        """
        # Simplified version:
        for entry in entries:
            try:
                self[entry.url.host] += [entry]
            except KeyError:
                self[entry.url.host] = [entry]
        
        
        temp_dict = {entry.url.host: [] for entry in entries}        
        for entry in entries:
            temp_dict[entry.url.host] += [entry]

        # Update the dictionary
        # self.update(temp_dict) # Will override any lists with the same host name
        for host, entry in temp_dict.items():
            #try:
            self[host] += [entry]
            #except IndexError:
            #self[host] = [entry]
    
    
            
    def save(self, scraper):
        """ Save the current state of a scraper. """
        entry = HistoryEntry(scraper.url, scraper.response)
        self.load_history_entries(entry)
    
    
    
#url = 'http://stackoverflow.com/'

#easy_url1 = parse_url(url)
#print easy_url1
#print easy_url1.__class__
#print repr(easy_url1)
#print easy_url1.geturl()
    
    
    
    
    
    
    
    
    