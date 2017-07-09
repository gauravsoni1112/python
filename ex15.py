#import argv module from the sys
from sys import argv

#define the input parameter for arguments
script, file_name = argv

#this is the module use to open the file and return file object 
txt = open(file_name)

print "Here's your file %r:" % file_name
#this is use to read the file object 
print txt.read()

print "Type the filename again:"

file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
