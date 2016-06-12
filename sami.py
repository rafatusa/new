def add(a,b):
    print "ADDING %d + %d " % (a,b)
    return a+b
def subtract(a,b):
    print "SUBSTRACT %d - %d " % (a,b)
    return a-b
def multiply(a,b):
    print "MULTIPLY %d * %d " % (a,b)
    return (a*b)
def divided(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a/b

print "Lets do some math with just functions!"

age =add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divided(100,2)

print "age: %d, height: %d, weight: %d, iq: %d" % (age,height,weight,iq)

print "Here is the puzzle"

what =add(age,subtract(hight,multiply(weight,divided(iq,2)))
print "That becomes: ", what, "Can you do that by hand?"

          
