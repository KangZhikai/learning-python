class Parent(object):
    
    def override(self):
        print "PARENT override()"
        
class Chile(Parent):
    
    def override(self):
        print "CHILE override()"

dad=Parent()
son=Chile()

dad.override()
son.override()