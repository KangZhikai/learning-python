#--conding:UTF8--
print "You enter a dark room,There are two doors:door1 and door2,which one do you want to enter"

door=raw_input(">")

if door=="1":
    print "There is a gaint bear in the room ,what would you do?"
    print "1.Take the cake"
    print "2.Scream to the bear"
    
    bear=raw_input(">")
    
    if bear=="1":
        print "The bear will eat your face off.Good job!"
    elif bear=="2":
        print "The bear will eat you head off.Good job!"
    else:
        print "Doing %s is probably good!"%bear
elif door=="2":
    print "You stare at ...."
    print "1.Blue"
    print "2.Yellow"
    print "3.Understading"
    
    insatiny=raw_input(">")
    if insatiny=="1" or insatiny=="2":
        print "Something is bad"
    elif insatiny=="2":
        print "Something is good."
    else:
        print "You are dead!"
        
        