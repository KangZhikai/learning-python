class Other(object):
    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
        
    def alerted(self):
        print "OTHER alerted()"
        
class Child(object):
    
    def __init__(self):
        self.other=Other()
    
    def override(self):
        print "CHILD overrider()"
    
    def implicit(self):
        self.other.implicit()
        
    def alerted(self):
        print "BEFORE CHILD alerted()"
        self.other.alerted()
        print "AFTER CHILD alerted()"
        
son=Child()
son.override()
son.implicit()
son.alerted()