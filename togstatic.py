# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd
import time
i = 0
j = 0
no_of_toggles = int(sys.argv[3])
no_of_routes = int(sys.argv[2])
switch = sys.argv[1]
static_route = ["enable","configure"]
nostatic_route = ['enable','configure']
type = sys.argv[4]
#for x in range(0,no_of_toggles):
for n in range(0,no_of_routes):      
   if i > 255:
      i = 0
      j = j+1
   noip_route1 = "no ip route 61.0." + str(j) + "." + str(i) + "/32" + " nexthop-Group " + type + str(n)
   static_route.append(noip_route1)
   i = i +1
i = 0
j = 0
for n in range(0,no_of_routes):
   if i > 255:
      i = 0
      j = j+1
   ip_route1 = "ip route 61.0." + str(j) + "." + str(i) + "/32" + " nexthop-Group " + type + str(n)
   nostatic_route.append(ip_route1)
   i = i+1

for x in range(0,no_of_toggles):
   capiCmd(switch,static_route)
   time.sleep(1)
   capiCmd(switch,nostatic_route)
   time.sleep(1)
print static_route
print nostatic_route
