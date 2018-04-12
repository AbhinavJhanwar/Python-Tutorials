'''
Created on Feb 23, 2017

@author: abhinav.jhanwar
'''

class Employee:
    'Common base class for all employees'
    empCount = 0        #to make empCount private we can write it as __empCount, to access it we can write as print emp1._Employee__EmpCount

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)
        
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name," destroyed")

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

#direct attribute adding/updating
emp1.age = 7  # Add an 'age' attribute.
print(emp1.age)
del emp1.age  # Delete 'age' attribute.

#attribute functions
print(hasattr(emp1, 'age'))    # Returns true if 'age' attribute exists
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
print(getattr(emp1, 'age'))    # Returns value of 'age' attribute
delattr(emp1, 'age')    # Delete attribute 'age'

#built-in class attribute
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
