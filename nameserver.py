#!/usr/local/bin/python3

import cgi

# program which interfaces python with http prodocol

# opens the etc/passwd
filename = '/etc/passwd'
fh = open(filename)


# creates and populates a list of usernames from etc/passwd by
# stripping and splitting the fh wrapper
userNameList = []
for line in fh:
    line = line.strip().split(':')
    userNameList.append(line[0])

# now we have a list which contains all the usernames. 
    
#receives the data from nameclient.py and strips and splits the wrapper
term = cgi.FieldStorage().getvalue('name') or 'goof'
term = term.strip().split(':')

# now we have a list of the argv elements

print('Content-type: text/plan\n')

# compares the argv elements to the etc/passwd username list and prints 
for name in term:
    if name in userNameList:
        print(name) 



