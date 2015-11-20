#!/usr/local/bin/python3

# Required: Submit as "largest" a program which identifies the single largest number occurring
# in the Urantia Book, as found in /user/abrick/resouces/urantia. Number is in the trillions

# Import the regular expression module. 
import re 

# Open the file which contains the urantia book.
fh = open('/users/abrick/resources/urantia')

# Assign a beginning largest number. 
largestNumber = 1

# Loop through the lines in the fh searching for lines with numbers in them.

for line in fh:

    # Only select lines in the fh which have numbers in them, and 
    # then strip the \n  and split the lines on a white space to create stringDigit elements.
    
    if len(re.findall('\d',line)) > 0:
        line = line.strip().split(' ')
            
            # Only select string elements which contain numbers in them. 
            # then strip '.' and spilt and rejoin to eliminate the commmas.
            # hint of word in the trillions allows to only look at lengths 
            # which are greater than 12.
  
        for word in line:
            if len(re.findall('\d',word)) > 12:
                word = word.strip('.').split(",")
                word = ''.join(word)
                # Convert string to an int for comparison. 
                try:
                    number = int(word)
                # Error handling takes care of non int exceptions like fractions/dashes etc...
                except ValueError:
                    number = 0
                # Compares the largestNumber to the current number under examination
                # and reassigns if required. 
                if largestNumber < number:
                    largestNumber = number

#Print output
print("The largest number in the Urantia book is ", largestNumber)


# Just for fun, we'll convert the integer to a string, and insert commas 
# so the largest number is persented in a way which is much easier on the eyes.
 
# Assign a counter, convert the largest number to a string and define
# the largestNumberAsStringWithCommas object.

counter = 0
largestNumberAsString = str(largestNumber)
largestNumberAsStringWithCommas = ''

# Loop though the largestNumberAsString starting from the end of the string.
for stringDigit in largestNumberAsString[::-1]:
    counter = counter + 1
    # Assemble the string backwards and insert commas after 3 stringDigits. 
    largestNumberAsStringWithCommas = largestNumberAsStringWithCommas + stringDigit
    if counter%3 == 0 and counter < len(str(largestNumber)):
        largestNumberAsStringWithCommas = largestNumberAsStringWithCommas + ','

# Flip largestNumberAsStringWithCommas  back to forwards after final construction of 
# largestNumberAsStringWithCommas

largestNumberAsStringWithCommas = largestNumberAsStringWithCommas[::-1]

#Print output
print('Or in a more human readable string with comma format ', largestNumberAsStringWithCommas)

