'''
Created on Feb 28, 2017

@author: abhinav.jhanwar
'''


fo = open("listTest.py","r+")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)

#fo.write( "Python is a great language.\nYeah its great!!\n")
str = fo.read(600)
print ("Read String is : ", str)

# Close opened file
fo.close()
