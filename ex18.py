#this one is like script with args
def print_two(*args):
   arg1, arg2 = args
   print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that * args is just pointless,we can just do this
def print_two_again(arg1, arg2):
   print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
   print "arg1: %r" % arg1

def print_none():
   print "I got nothing"

print_two("Gaurav","Soni")
print_two_again("Gaurav","Soni")
print_one("Gaurav")
print_none()

