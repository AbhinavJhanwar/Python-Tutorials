'''
Created on Feb 22, 2017

@author: abhinav.jhanwar
'''


#Python lists

list_set = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

# Prints complete list
print(list)
# list can be modified
list_set[0] = 89.3
# adding elements in list
list_set = list_set+['mike']
# Prints first element of the list
print(list_set[0])
# Prints elements starting from 2nd till 3rd
print(list_set[1:3])
# Prints elements starting from 3rd element
print(list_set[2:])
# Prints list two times
print(tinylist * 2)
# Prints concatenated lists
print(list_set + tinylist)

# using list comprehension
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i, j, k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n])
