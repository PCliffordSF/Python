#!/usr/local/bin/python3

print('Content-type: text/html\n')

import time
import cgi

filepath = '/tmp/paulsstorage.txt'
storagefile = open(filepath, 'a')
 
    
#receives the data from nameclient.py and strips and splits the wrapper
message = cgi.FieldStorage().getvalue('key') or ''
retrieve = cgi.FieldStorage().getvalue('key2') or ''

time = time.time()

storagefile.write(message + '\n')
print('it worked')

storagefile.close()

if retrieve == 'true':
    retrieveMessages = open(filepath).read()
    print(retrieveMessages)


