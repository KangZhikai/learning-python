#--coding:utf-8--
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
    def override(self):
        print "PARENT override()"
    def alerted(self):
        print "PARENT alerted()"
        
class Child(Parent):
    def override(self):
        print "CHILD override()"
    def alerted(self):
        print "BEFORE CHILD alerted()"
        super(Child,self).alerted()
        print "AFTER CHILD alerted()"
        
dad=Parent()
son=Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.alerted()
son.alerted()