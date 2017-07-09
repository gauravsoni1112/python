from sys import argv

script, file_name = argv

print "We are going to erase %r." % file_name
print "If you dont want to do that ,hit ctrl-C."
print "If you do want hit RETURN."

raw_input("?")

print "Opening a file...."
target = open(file_name,'w')

print "Truncating a file.GoodBye! "
target.truncate()

print "Now I am going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Writing the lines in the file"

target.write(line1+"\n")
#target.write("\n")
target.write(line2+"\n")
#target.write("\n")
target.write(line3+"\n")
#target.write("\n")

#for i in range(3)
#   target.write(line

print "Printing done..Closing the file"

target.close()
