# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

i = 0
j = 0
type = sys.argv[3]
no_of_routes = int(sys.argv[2])
switch = sys.argv[1]
static_route = ["enable","configure"]
for n in range(0,no_of_routes):
   ip_route1 = "ipv6 route 3000::" + str(i) + "/128" + " nexthop-Group" + " " + type + str(n)
   static_route.append(ip_route1)
   i = i+1
#print static_route
capiCmd(switch,static_route)
