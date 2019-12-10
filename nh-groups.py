# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd
switch = sys.argv[1]
nexthopgroup_list = ['enable','configure']
type = "ip"
for i in range(6,100):
   nexthopgroup_list.append("no nexthop-group " + type + str(i) + " " +  "type" + " " + type)
   #nexthopgroup_list.append("entry 0 nexthop 11.0.3.0")
print nexthopgroup_list
capiCmd(switch,nexthopgroup_list)


