class Parent(object):
    def alerted(self):
        print "PARENT alerted()"
        
class Child(Parent):
    def alerted(self):
        print "CHILD,BEFORE PARENT alerted()"
        super(Child,self).alerted()
        print "CHILD,AFTER PARENT alerted()"
        
dad=Parent()
son=Child()

dad.alerted()
son.alerted()