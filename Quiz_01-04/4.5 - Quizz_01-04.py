import dateutil
import datetime as dt
import calendar
import time
from dateutil import parser


#Using the Python calendar library and given a year check if it is a leap year printing True (leap year) or False.

year = int(input("Year:"))
print(calendar.isleap(year))

#Using the Python time library convert a given number of seconds since the epoch to a time struct_time
seconds = int(input("Number of seconds since the epoch:"))
print(time.gmtime(seconds))

#Given a date string in the following format ("17/02/2022 14:30:45") add a given number of weeks, days, hours and seconds (all integer values) and print the new date using the same format. (using the Python datetime library)
Date = input("Date:")
Weeks = input("Weeks:")
Days = input("Days:")
Hours = input("Hours:")
Seconds = input("Seconds:")
date = dt.datetime.strptime(Date, "%d/%m/%Y %H:%M:%S")

date = date + dt.timedelta(weeks = int(Weeks), days = int(Days), hours = int(Hours), seconds = int(Seconds))
print(date.strftime("%d/%m/%Y %H:%M:%S"))

#Given two date strings in iso format and the corresponding timezones, calculate the difference between the two dates (date2 > date1). (Using datetime and dateutil libraries)
Date1 = input("Date1:")
Timezone1 = input("Timezone1:")
Date2 = input("Date2:")
Timezone2 = input("Timezone2:")
date1 = dateutil.parser.parse(Date1)
date2 = dateutil.parser.parse(Date2)
date1 = date1.replace(tzinfo = dateutil.tz.gettz(Timezone1))
date2 = date2.replace(tzinfo = dateutil.tz.gettz(Timezone2))
print(date2 - date1)
