# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

co_ios = "Cisco IOS Software, C880 Software (C880DATAUNIVERSALK9-M),Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
temp = co_ios.split(',')
for each in temp:
   if 'Version' in each:
      print 'ios-version %s' %(each.split()[-1])
