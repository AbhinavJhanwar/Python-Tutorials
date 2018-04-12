'''
Created on Feb 23, 2018

@author: abhinav.jhanwar
'''

# [1] using lambda function
f = lambda x, y : x + y
#print(f(1,1))

# [2] using lambda function with map with 1 argument
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5, 39)
F = list(map(fahrenheit, temp))
C = list(map(celsius, temp))
#print(F)
#print(C)

F = list(map(lambda T: (float(9)/5)*T+32, temp))
#print(F)
C = list(map(lambda T: (float(5)/9)*(T-32), temp))
#print(C)

# [3] using lambda function with map with more than 1 arguments
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
#print(list(map(lambda x,y:x+y, a,b)))
#print(list(map(lambda x,y,z:x+y+z, a,b,c)))
#print(list(map(lambda x,y,z:x+y-z, a,b,c)))

# [4] using lambda with filter
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = list(filter(lambda x: x % 2, fib))
#print(result)
result = list(filter(lambda x: x % 2 == 0, fib))
#print(result)

