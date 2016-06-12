import sys

if len(sys.argv) > 1:
    name =sys.argv[1]
else:
    name=raw_input("enter your name : ")


if len(sys.argv) > 2:
    age=int(sys.argv[2])
else:
    age=int(raw_input("enter your age: "))


sayHello = "Hello " + name + ","

if age ==100:
    sayAge ="you allready 100 years old!"
elif age < 100:
    sayAge="you will be 100 in " + str(100 - age) + ' years !'
else:
    sayAge="you truned 100, almost like " + str(age - 100) + ' years ago!'

print sayHello , sayAge
