'''
Created on Feb 21, 2017

@author: abhinav.jhanwar
'''

#variable types
#variable assignments
print("#variable assignments")
var1 = 78           #integer
var2 = 9536.5       #float
var3 = "Hello"      #string
var4 = 8+6j         #complex number
print (var1)
print (var2)
print (var3)
print (var4)



#multiple assignments
print("\n#multiple assignments")
a=b=c=1
print (a, b, c)

a,b,c=1,2,"Hello"       #a=1, b=2, c="Hello"
print(a, b, c)

#deleting an object
del var1


print (locals())