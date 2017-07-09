from sys import argv
from os.path import exists


scrip, from_file, to_file = argv

print "Copying from %s to %s" % (from_file,to_file)

in_file = open(from_file)
in_data = in_file.read()


print "The input file is %d bytes long" % len(in_data)

print "Does the output file exists? %r" % exists(to_file)

print "Ready ,hit RETURN to continue else CTRL C"

raw_input("?") 

output_file = open(to_file,'w')
output_file.write(in_data)


print "Alright all done"

output_file.close()
in_file.close()
