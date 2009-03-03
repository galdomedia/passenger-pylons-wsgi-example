import os, sys                                                                                                                                          
sys.path.append('/Users/maciejlitwiniuk/Sites/passenger-pylons-wsgi-example')                                                                     
os.environ['PYTHON_EGG_CACHE'] = '/Users/maciejlitwiniuk/Sites/eggs'                                                           
from paste.deploy import loadapp                                                                                                                        
                                                                                                                                                        
def application(environ, start_response):                                                                                                               
    environ['SCRIPT_NAME'] = environ['PATH_INFO']                                                                                                       
    application = loadapp('config:/Users/maciejlitwiniuk/Sites/passenger-pylons-wsgi-example/development.ini')                                    
    return application(environ, start_response)