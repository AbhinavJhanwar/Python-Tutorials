'''
Created on Feb 22, 2017

@author: abhinav.jhanwar
'''
import time;
import string

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

import calendar

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)

