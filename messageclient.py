#!/usr/local/bin/python3

# imports the needed stuff. :-)
from sys import argv
import urllib.request
import urllib.parse 




#creates a single string of command line arguments. 
# join on ':' which we know is the etc/passwd delimiter, so this is
# a safe delimiter.
nameDict = {}
nameDict['key'] = ''
nameDict['key2'] = 'false'

if argv[1] == '-r':
    nameDict['key2'] = 'true'
else:  
    names = ' '.join(argv[1::])
    nameDict['key'] = names

# converts the dictionary into key value pairs to send to server. 
namePair = urllib.parse.urlencode(nameDict)


#creates the url string eith key-value pair
url = 'http://hills.ccsf.edu/~pcliffor/cgi-bin/messageserver.py?' + namePair


#requests from the server
request = urllib.request.urlopen(url).read()

#prints the serverside output
print(request.decode('utf-8'))
