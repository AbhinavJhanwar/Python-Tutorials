'''
Created on Feb 28, 2017

@author: abhinav.jhanwar
'''

#!/usr/bin/python3
import os

# This would  remove "test"  directory.
os.rmdir( "test"  )

# Create a directory "test"
os.mkdir("test")

# Changing a directory to "/home/newdir"
os.chdir("test")

# This would give location of the current directory
print (os.getcwd())