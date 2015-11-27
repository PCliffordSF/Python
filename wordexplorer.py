#!/usr/local/bin/python3

import cgi

# program which interfaces python with http. 
# program isn't useful, but good to keep around 

filename = '/users/abrick/resources/insane-ascii'
fh = open(filename)
term = cgi.FieldStorage().getvalue('key') or 'goof'

print("Content-type: text/html\n")

contains = []
containedBy = []

for line in fh:
    line = line.strip()
    if term in line:
        containedBy.append(line)       
        #print('<a href=?insane=' + line + '>' + line + '</a><br/>')   
    if line in term:
        contains.append(line)
        #print('<a href=?insane=' + line + '>' + line + '</a><br/>')
        #print(' is contained by ' + term) 

fh.close()

for word in containedBy:
    print(term + ' is contained by ')
    print('<a href=?key=' + word + '>' + word + '</a><br/>')
    #print(word)

for word in contains:
    print(term + ' contains ')
    print('<a href=?key=' + word + '>' + word + '</a><br/>')





