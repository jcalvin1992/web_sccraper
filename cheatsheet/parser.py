from bs4 import BeautifulSoup as BS




class TerminalDeubger(object):
    """ A class that provides some useful debugging methods """
    
    # Shortcuts
            success_message = '[+] Success {var_name}'
    ):
        """ Message the status of a variable, if False, close program. """
        self.show_type(var, var_name)  
        if not var:  self.exit_message(failed_message.format(var_name=var_name))
        self.message(success_message.format(var_name=var_name))     
        
        
    # Features
    def message(self, message):
        """ A simple print message """
        print message

    def message_locating_variable(self, var_name):
        print '[?] Locating ' + var_name

        
    def exit_message(self, message):
        self.message(message)
        import sys
        sys.exit(1)
        
    

    def show_type(self, var, var_name=None):
        """ print out the variables type """
        if var_name:
            print '[!] ' + var_name + ' = ' + str(type(var))
        else:
            print '[!] Type: ' + str(type(var))
            
            
    def get_type(self, var):
        """ return the variables type """
        return type(var)

    def compare_types(self, var1, var2):
        """ Return True if var1 and var2 share the same type, or else False """
        return var1 == var2
    
    

    
    
    
    
    
    
class ParsingHandle(object):
    """ 
    A base class that must have its handle() method overriden.
    The overriden handle() should mine data from a BeautifulSoup object.
    """
    
    def __init__(self, name, handle_function=None, url=None):
        """ 
        Ovverride the handle method with a pre-exsiting function
        that is passed in as an argument when initializing.
        """
        self.name = name # should explain this handle, also the key for ParsingManager
        if handle_function:
            self.handle = handle_function

    def handle(self, soup):
        pass






class ParsingManager(dict):
    """ Should be able to """
    
    def __init__(self, *parsing_handles):
        super(ParsingManager, self).__init__({
            handle.name: handle 
              for handle in parsing_handles
        })
    
    def add_handle(self, handle):
        self[handle.name] = handle
        
    def call_handle_by_name(self, name, soup):
        if name in self:
            return  self[name].handle(soup)
        else: 
            print 'Error: No Handle Named \'%s\'' % name
            return None

    
    def get_handle_by_name(self, name):
        try: 
            parsing_handle = self[name]
            parsing_handle == True # If False, will jump to excpt code block
            return parsing_handle
        except Exception, e: 
            print 'Error Getting Handle \'%s\': %s' % (name, str(e)) 
            return None
    
    
    



        




