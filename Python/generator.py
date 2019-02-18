# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:10:56 2019

@author: abhinav.jhanwar
"""

# yield works similar to return
# instead of terminating the function yield just pause the function and saves the current state and return
# when function is called again then it continues from the previously saved state

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
# It returns an object but does not start execution immediately.
a = my_gen()

# We can iterate through the items using next().
next(a)
# Once the function yields, the function is paused and the control is transferred to the caller.

# Local variables and theirs states are remembered between successive calls.
next(a)

next(a)

# Finally, when the function terminates, StopIteration is raised automatically on further calls.
next(a)

# Using for loop
for item in my_gen():
    print(item) 
 
############################## EXAMPLE 2 ########################
def my_gen(limit):
  data = 1
  while data < limit:
    yield data
    data += 2
    
gen_obj = my_gen(10)
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

for item in my_gen(12):
    print(item)