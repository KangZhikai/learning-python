#--coding:utf-8--
class Thething(object):
    def __init__(self):
        self.number=0
        
    def some_function(self):
        print "I got some function"
    
    def add_me_more(self,more):
        self.number+=more
        return self.number
    
#Two different things
a=Thething()
b=Thething()

a.some_function()
b.some_function()

print a.add_me_more(40)
print b.add_me_more(50)

print a.number
print b.number

class TheMuliter(object):
    
    def __init__(self,base):
        self.base = base
    
    def do_it(self,m):
        return m*self.base
x=TheMuliter(a.number)
print x.do_it(b.number)

