from sys import argv

#assign the input parameters
script, file_name = argv


#read the file
print "reading the file %s" % file_name

file = open(file_name,"r")

for line in file:
   print line,

