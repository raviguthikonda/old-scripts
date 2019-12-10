# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd
import time

switch = sys.argv[1]
nhgs = int(sys.argv[2])  #no of next-hop groups
nhentries = int(sys.argv[3]) #no of entries in each next-hop group
nexthopgroup_list = ['enable','configure']
nonexthopgroup_list = ['enable','configure']
type = sys.argv[4]
toggles = int(sys.argv[5])
for i in range(0,nhgs):
   if type == 'ip':
      nexthopgroup_list.append("nexthop-group " + type + str(i) + " " +  "type" + " " + type)
      k = 0 
      l = 0
      for j in range(0,nhentries):
         if k > 255:
            k = 0
            l = l+1
         nexthopgroup_list.append("entry " + str(j) + "  nexthop" + "  150." + str(l) + "." + str(k) + ".15")
         #nexthopgroup_list.append("entry " + str(j) + "  nexthop" + "  11.11.11." + str(k) )
         k = k+1
   elif type == "ip-in-ip":
      nexthopgroup_list.append("nexthop-group " + type + str(i) + " " + "type" + " " + type)
      nexthopgroup_list.append("tunnel-source" + "  200.200.200.200")
      #nexthopgroup_list.append("no size")
      #nexthopgroup_list.append("size "+ str(nhentries))
      k = 0
      l = 0
      for j in range(0,nhentries,2):
         if k > 255:
            k = 0
            l = l+1
         #nexthopgroup_list.append("tunnel-source" + "  150." + str(l) + "." + str(k) + ".1")
         nexthopgroup_list.append("entry " + str(j) + "  tunnel-destination" + "  150." + str(l) + "." + str(k) + ".15")
         nexthopgroup_list.append("entry " + str(j+1) + "  tunnel-destination" + "  150." + str(l) + "." + str(k) + ".15")      
         k = k+1
   elif type == "gre":
      nexthopgroup_list.append("nexthop-group " + type + str(2) + " " + "type" + " " + type)
      #nexthopgroup_list.append("no size ") #+ str(nhentries))
      k = 254
      l = 3
      for j in range(0,nhentries):
         if k > 255:
            k = 0
            l = l+1
         nexthopgroup_list.append("tunnel-source" + "  150." + str(l) + "." + str(k) + ".1")
         nexthopgroup_list.append("entry " + str(j) + "  tunnel-destination" + "  150." + str(l) + "." + str(k) + ".15")
         #nexthopgroup_list.append("entry " + str(j+1) + "  tunnel-destination" + "  150." + str(l) + "." + str(k) + ".15")
         k = k+1
for i in range(0,nhgs):
   if type == 'ip':
      nonexthopgroup_list.append("nexthop-group " + type + str(i) + " " +  "type" + " " + type)
      k = 0
      l = 0
      for j in range(0,nhentries):
         if k > 255:
            k = 0
            l = l+1
         nonexthopgroup_list.append("entry " + str(j) + "  nexthop" + "  150." + str(l) + "." + str(k) + ".15")
         #nexthopgroup_list.append("entry " + str(j) + "  nexthop" + "  11.11.11." + str(k) )
         k = k+1
   elif type == "ip-in-ip":
      nonexthopgroup_list.append("nexthop-group " + type + str(i) + " " + "type" + " " + type)
      nonexthopgroup_list.append("tunnel-source" + "  200.200.200.200")
      #nexthopgroup_list.append("no size")
      #nexthopgroup_list.append("size "+ str(nhentries))
      k = 0
      l = 0
      for j in range(0,nhentries,2):
         if k > 255:
            k = 0
            l = l+1
         #nexthopgroup_list.append("tunnel-source" + "  150." + str(l) + "." + str(k) + ".1")
         nonexthopgroup_list.append("no entry " + str(j) + "  tunnel-destination" + "  150." + str(l) + "." + str(k) + ".15")
         nonexthopgroup_list.append("no entry " + str(j+1) + "  tunnel-destination" + "  150." + str(l) + "." + str(k) + ".15")
         k = k+1
   elif type == "gre":
      nexthopgroup_list.append("nexthop-group " + type + str(2) + " " + "type" + " " + type)
      #nexthopgroup_list.append("no size ") #+ str(nhentries))
      k = 254
      l = 3
      for j in range(0,nhentries):
         if k > 255:
            k = 0
            l = l+1
         nexthopgroup_list.append("tunnel-source" + "  150." + str(l) + "." + str(k) + ".1")
         nexthopgroup_list.append("entry " + str(j) + "  tunnel-destination" + "  150." + str(l) + "." + str(k) + ".15")
         #nexthopgroup_list.append("entry " + str(j+1) + "  tunnel-destination" + "  150." + str(l) + "." + str(k) + ".15")
         k = k+1
#print nexthopgroup_list
#print nonexthopgroup_list
for x in range(0,toggles):
   capiCmd(switch,nexthopgroup_list)
   time.sleep(1.1)
   #capiCmd(switch,nonexthopgroup_list)
