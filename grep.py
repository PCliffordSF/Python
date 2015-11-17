#!/usr/local/bin/python3
# this was an in class assignment which replicates the linux grep program. Since there will never be a use case for this,
# I'm not going to clean it up or comment it. Fun program to write and takes advantage of some cool python features. 
# This project was part of our error handling studies. 

import sys
from sys import argv

fileList = []
lineCounter = 0

try:
    test = argv[2]
except IndexError:
    print("you're a dummy, not enough arguments")
    sys.exit()
    
if argv[1] == '-v':
    n = 3
else:
    n = 2

def grep(n):
    for item in argv[n::]:
        filename =  item
        try:
            fh = open(filename)
            fileList.append(filename)       
        except FileNotFoundError:
            print("file not found")
        except PermissionError:
            print("you don't have permission for", filename)
        fh.close()

def outputline(n):
    lineCounter = 0
    for file in fileList:
        fh = open(file)
        for line in fh:
            lineCounter += 1
            line = line.strip()
            if n == 2:
                if argv[1] in line:
                    seq = (file, str(lineCounter) ,line)
                    outputLine = ':'.join(seq)    
                    print(outputLine)
            else:
                if argv[2] not in line:
                    seq = (file, str(lineCounter), line)
                    outputLine = ':'.join(seq)
                    print(outputLine) 
  
grep(n)
outputline(n)
