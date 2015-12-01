#!/usr/local/bin/python3

# imports the needed stuff. :-)
from sys import argv
import urllib.request
import urllib.parse 

#creates a single string of command line arguments. 
# join on ':' which we know is the etc/passwd delimiter, so this is
# a safe delimiter.  
names = ':'.join(argv[1::])

#creates the url string eith key-value pair
url = 'http://hills.ccsf.edu/~pcliffor/cgi-bin/nameserver.py?name=' + names


#requests from the server
request = urllib.request.urlopen(url).read()

#prints the serverside output
print(request.decode('utf-8'))
