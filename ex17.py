#--coding:utf-8--
class Animal(object):
    pass

class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
        
    def sing_me_song(self):
        for line in self.lyrics:
            print line
have_a_song=Song(["Happy birthday to you",
                             "You are my master",
                             "And I'll do everything for you"])

class Dog(Animal):
    def __init__(self,name):
        self.name=name
        print self.name
    def dance_dog(self,name):
        print "Hey,I'm a dancing dog,I can do lots of things,place type following numbers:"
        print "1.Dance"
        print "2.Sing a Song"
        print "3.Draw a picture"
        
        choices=raw_input("Please type some number")
        if choices=="1":
            print "Dance Dance And Dance"
        elif choices=="2":
            have_a_song.sing_me_song()
        elif choices=="3":
            print "I will draw a picture for you!"
        else:
            print"Please type a number"
        
        
class Cat(Animal):
    def __init__(self,name):
        self.name=name
        
class Person(object):
    def __init__(self,name):
        self.name=name
        
        self.pet=None
        
class Employee(Person):
    def __init__(self,name,salary):
        super(Employee,self)._init_(name)
        
        self.salary=salary
        
class Fish(object):
    pass

class Salom(Fish):
    pass

class Halibuat(Fish):
    pass

#rover is a dog
rover=Dog("Rover")
rover.dance_dog("Rover")

#saten is a cat
saten=Cat("Saten")

marry=Person("Marry")

    