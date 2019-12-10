# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'

list = uptime1.split("is")
print type(list[1])
list1 = list[1].split(',')
print list1
for each in list1:
   temp = each.strip()
   print temp
   if 'weeks' in temp:
      weeks = temp.split(" ")[0]
   if 'days' in temp:
      days = temp.split(" ")[0]
   if 'hours' in temp:
      hours = temp.split(" ")[0]
   if 'minutes' in temp:
      minutes = temp.split(" ")[0]
try:
   time = int(weeks)*7*24*60*60 + int(days)*24*60*60 + int(hours)*60*60
except ValueError as e:
   print str(e)
print "time in seconds is: %s" %(time)
device_name = list[0].split(" ")[0]
dict = {device_name:time}
print dict

