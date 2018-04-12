'''
Created on Feb 23, 2017

@author: abhinav.jhanwar
'''

class Parent:        # define parent class
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(self):
        print ('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)
        
    def myMethod(self):
        print ("inside parent myMethod")
        
class Parent1:        # define parent class
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(self):
        print ('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = 500

    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)

class Child(Parent1, Parent): # define child class        #multiple inheritance handled as first class methods are used.
    def __init__(self):
        print ("Calling child constructor")

    def childMethod(self):
        print ('Calling child method')
        
    def myMethod(self):
        print("inside child myMethod")

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
c.myMethod()