'''
Created on Jul 11, 2018

@author: abhinav.jhanwar
'''

from datetime import datetime
import pytz


# set time zone
timezone = pytz.timezone('Asia/Calcutta')
# localize time as per the timezone
syncDate = timezone.localize(datetime.now())
# format the time as per requirement
syncDate = syncDate.strftime('%Y-%m-%dT%H:%M:%S')
# creating a new date time object as per user
newDate = datetime(2018, 7, 10, 12, 43, 54)
# creating datetime object from string
datetime.strptime("23-01-2198","%d-%m-%Y")
    
