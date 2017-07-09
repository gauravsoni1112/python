#utility to read the files
from sys import argv

script, file_name = argv

#print the full file function by passing file object
def print_all(f):
  print f.read()

#print the file in reverse
def rewind(f):
  print f.seek(0)

current_file = open(file_name)



print "Print the whole file"

print_all(current_file)
rewind(current_file)
print_all(current_file)

print "Print the rewind ,kind of like tape."

rewind(current_file)
