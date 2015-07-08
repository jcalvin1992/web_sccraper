    

from parser import ParsingHandle, ParsingManager, TerminalDeubger




class StackOverFlow_HomeQuestion(object):
    """ A container for questions that are scraped from the home page. """
    
    def __init__(self, name='question name', tags=[], 
        author_name='author name', author_reputation=0,
        votes=0, answers=0, views=0
    ):
        
        self.name = name
        self.tags = tags
        self.author_name = author_name
        self.author_reputaion= author_reputation
        self.votes = votes
        self.answers = answers
        self.views = views
            
        
    def __unicode__(self):
        return unicode(
            '<StackOverFlow_HomeQuestion: name=%s, views=%d>' % 
            (self.name, self.views))
    
    def __str__(self):
        return self.__unicode__()
    
    




class StackOverFlow_HomeQuestions_Handle(TerminalDeubger, ParsingHandle):
    """ Gather the questions listed on http://stackoverflow.com/ """
    def __init__(self):
        super(StackOverFlow_HomeQuestions_Handle, self).__init__(
        'Home Questions')
        
        
        
        
    def convert_k_to_int(self, number):
        """
        Stack overflow uses a 'k' to represent a thousand.
        Strip the k, and multiply the number by 1000
        """
        number = str(number).lower()
        if number[-1] == 'k':
            number = int(number[:-1])
            number *= 1000
        return int(number)
            
    
    
    
    
    def handle(self, soup):
    
        # self.message_Top_ClassHandle()
        self.message('[+] Top of %s.handle(...)' % self.__class__.__name__)
        # self.message_Inside_ClassHandle()
        # - self.message('[+] Inside %s .handle(...)' % self.__class__.__name__) 
        
        # self.message_locating_variable('questions_container')
        
        
        # container holding all questions
        self.message_locating_variable('questions_container') 
        questions_container = soup.find(
            'div', 
            attrs = {
                'id':'question-mini-list'
            }
        )
        self.debug_status_exit_on_none(questions_container, 'questions_container')
        
        
        # list of question containers
        self.message_locating_variable('question_containers') 
        question_containers = questions_container.find_all(
            'div', 
            attrs = {
                'class':'question-summary narrow'
            }
        )
        self.debug_status_exit_on_none(question_containers, 'question_containers')      
        
        # List StackOverFlow_HomeQuestion()'s
        self.message_locating_variable('questions')
        questions = []
        
        # Scaraping / Storing data from a question container using 
        for container in question_containers:
            
            #container = BS(container)
            self.show_type(container)
            
            # Seperate our conatiner into sub containers
            stats = container.find('div', attrs={'class':'cp'})
            details = container.find('div', attrs={'class':'summary'})
            

            # stats
            votes = stats.find('div', attrs={'class':'votes'}).div.span.text
            answers = stats.div.next_sibling.next_sibling.div.span.text
            views = stats.find('div', attrs={'class':'views'}).div.span.text

            # stackoverflow represents thousnads with a K, strip 
            # the k then multiply the left over number by 100
            votes = self.convert_k_to_int(votes)
            answers = self.convert_k_to_int(answers)
            views = self.convert_k_to_int(views)



            # details
            name = details.h3.a.text
            tags = [tag.text for tag in details.div.find_all('a')]
            author_name = details.div.next_sibling.next_sibling.find(
                'a', 
                attrs = {
                    'class':None
                }
            )
            
            author_reputation = details.find(
                'span', 
                attrs = {
                    'class':'reputation-score'
                }
            ).text
            #author_reputation = int(details.div.next_sibling.next_sibling.span.next_sibling.text)

            
            # Storing Data That Was Scraped From HTML
            questions += [StackOverFlow_HomeQuestion(
                              name=name, tags=tags, 
                              author_name=author_name, 
                              author_reputation=author_reputation, 
                              votes=votes, answers=answers, views=views
                              )
                          ] 
        # End For Loop
        self.debug_status_exit_on_none(questions, 'questions')         

        return questions
    
    
    
    




# List of our parising handles
stackoverflow_handles = [StackOverFlow_HomeQuestions_Handle()]


# Loading our stack overflow ParsingManager()
stackoverflow_parsing_manager = ParsingManager( *stackoverflow_handles )

    
    
    
    