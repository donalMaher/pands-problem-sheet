#G00387859 DONAL MAHER
"""
Weekly task 5
Write a program that outputs whether or not today is a weekday.

"""

import datetime
#import the datetime function
#create a case statement to check the integer value 
#retruned from the datetime function 0 -4 weekday , 5 & 6 are the weekend
def isWeekDay():
    now = datetime.datetime.now()
    dayOfTheWeek = datetime.datetime.weekday(now)
    if dayOfTheWeek == 0 :
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 1:
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 2:
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 3:
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 4:
        print("Yes, unfortunately today is a weekday.")
    elif dayOfTheWeek == 5:
        print("It is the weekend, yay!")
    elif dayOfTheWeek == 6:
        print("It is the weekend, yay!")
isWeekDay()




        



