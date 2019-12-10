# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

no_of_linecards = int(sys.argv[2])
no_of_vrfs = int(sys.argv[3])
switch = sys.argv[1]
for n in range(3,no_of_linecards):
   static_route = ["enable","configure"]
   print n
   l = 1
   for r in range(1,no_of_vrfs):
      ip_route1 =  "ip route vrf vrf-" + str(r) + " " + "11." + str(n) + "." +str(n) + ".10/31" + " " + "11." +str(n) + ".0." + str(l)
      static_route.append(ip_route1)
      l = l+2
   print static_route
   capiCmd(switch,static_route)
   static_route = ["enable","configure"]
   l = l-3
   for r in range((no_of_vrfs),1,-1):
      ip_route1 =  "ip route vrf vrf-" + str(r) + " " + "11." + str(n) + "." +str(n) + ".0/31" + " " + "11." +str(n) + ".0." + str(l)
      static_route.append(ip_route1)
      l = l-2
   print static_route
   capiCmd(switch,static_route)
