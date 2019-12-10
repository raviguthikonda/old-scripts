# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

i = 0
j = 0
payloadtype = sys.argv[3]
no_of_nhg = int(sys.argv[2])
switch = sys.argv[1]
mpls_static_route = ["enable","configure"]
if payloadtype == 'ipv4':
   for n in range(0,no_of_nhg):
      if i > 255:
         i = 0
         j = j+1
      mpls_route = "mpls static top-label" + " " + str(n+16) + " " + "1.1.1.1 " + "pop payload-type ipv4"
      #mpls_route = "mpls static top-label" + " " + str(n+16) + " " + "51.0." + str(j) + "." + str(i) + " " + "pop payload-type ipv4"
      mpls_static_route.append(mpls_route)
      i = i+1
elif payloadtype == 'ipv6':
   for n in range(0,no_of_nhg):
      mpls_route = "mpls static top-label" + " " + str(n+16) + " " + "1111::1111"  + " " + "pop payload-type ipv6"
      mpls_static_route.append(mpls_route)
      i = i+1
print mpls_static_route
capiCmd(switch,mpls_static_route)
