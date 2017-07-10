def add(a, b):
  print "Adding %d + %d" % (a, b)
  return a+b

def substract(a, b):
  print "Substracting %d - %d" % (a, b)
  return a - b

def multiply(a, b):
  print "Multiplying %d * %d" % (a, b)
  return a * b

def divide(a, b):
  print "Divide %d / %d" % (a, b)
  return a / b

print "lets do some match with just functions!!!!"


age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

val = int(raw_input("???"))

#my divide by zero check
temp = divide(100, val)

print "Age is %d ,height is %d, weight is %d and iq is %d" % (age, height, weight, iq)

what = add(age, substract(height, multiply(weight,divide(iq,2))))

print "what is %d" % what
