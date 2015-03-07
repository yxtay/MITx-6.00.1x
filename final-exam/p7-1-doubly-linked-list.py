class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    if newFrob.myName() < atMe.myName():
        prevFrob = atMe.getBefore()
        while prevFrob and newFrob.myName() < prevFrob.myName():
            atMe = prevFrob            
            prevFrob = atMe.getBefore()
        if prevFrob:
            prevFrob.setAfter(newFrob)
            newFrob.setBefore(prevFrob)
        newFrob.setAfter(atMe)
        atMe.setBefore(newFrob)
    else:
        nextFrob = atMe.getAfter()
        while nextFrob and newFrob.myName() > nextFrob.myName():
            atMe = nextFrob
            nextFrob = atMe.getAfter()
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
        if nextFrob:
            newFrob.setAfter(nextFrob)
            nextFrob.setBefore(newFrob)
        
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    prevFrob = start.getBefore()
    if prevFrob:
        return findFront(prevFrob)
    else:
        return start
