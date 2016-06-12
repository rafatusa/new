import sys

vaildPassword = 'lola' #this is our password
inputPassword = raw_input ("please Enter Password:")

if inputPassword ==vaildPassword :
    print "you have access"

else:
    print "access denied"
    sys.exit(0)

print "welcome!"
