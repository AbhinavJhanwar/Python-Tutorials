'''
Created on Feb 22, 2017

@author: abhinav.jhanwar
'''

#python dictionary

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

#string formatting operator
print ("\n\nMy name is %s and weight is %d kg!" % ('Zara', 21))

#triple quotes
para_str = """\n\nthis is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str) 

#r'expression'
print ('C:\\nowhere')
print (r'C:\\nowhere')