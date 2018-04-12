'''
Created on Mar 22, 2018

@author: abhinav.jhanwar
'''

# creating set
myset = {1, 2} # Directly assigning values to a set
myset = set()  # Initializing a set
myset = set(['a', 'b']) # Creating a set from a list
print(myset)

# using add function
print('add')
myset.add('c')
print(myset)
myset.add('a') # As 'a' already exists in the set, nothing happens
myset.add((5, 4))
print(myset)

# using update function
print('update')
myset.update([1, 2, 3, 4]) # update() only works for iterable objects
print(myset)
myset.update({1, 7, 8})
print(myset)
myset.update({1, 6}, [5, 13])
print(myset)

# removing elements
# Both the discard() and remove() functions take a single value as an argument and removes that value from the set.
# If that value is not present, discard() does nothing, but remove() will raise a KeyError exception.
# .pop() This operation removes and return an arbitrary element from the set.
print('remove')
myset.discard(10)
print(myset)
myset.remove(13)
print(myset)
element = myset.pop()
print(element)
print(myset)
 

# Using union(), intersection() and difference() functions.
print('common set functions')
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
print(a.union(b)) # Values which exist in a or b
print(a|b)      # another way of union, only applicable on set of elements of set
print(a.intersection(b)) # Values which exist in a and b
print(a & b) # another way of intersection, only applicable on set of elements of set
print(a.difference(b)) # Values which exist in a but not in b{9, 5} 
print(a-b) # another way of difference, only applicable on set of elements of set
print(a.symmetric_difference(b))# values which are either in a or b but not in both
print(a^b)  # another way of symmetric_intersection






