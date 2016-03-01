#!/usr/bin/python
#import sys
#import logging
#logging.basicConfig(stream=sys.stderr)
#sys.path.insert(0,"/var/www/catalog/")

#from catalog import app as application
#application.secret_key = 'super_secret_key'

def application(environ, start_response):
    status = '200 OK'
    output = 'Catalog'

    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
