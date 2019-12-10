# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

i = 0
j = 0
no_of_nhgs = int(sys.argv[2])
switch = sys.argv[1]
nhg_list = ["enable","configure"]
type = sys.argv[3]
for n in range(1,no_of_nhgs):
   nhg = "no nexthop-Group" + " " + type + str(n)
   nhg_list.append(nhg)
#print static_route
capiCmd(switch,nhg_list)
