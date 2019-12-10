# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd
import time
switch = sys.argv[1]
nhgs = int(sys.argv[2])  #no of next-hop groups
toggles = int(sys.argv[3])
nexthopgroup_list = ['enable','configure']
type = sys.argv[4]
for i in range(0,nhgs):
   nexthopgroup_list.append("nexthop-group " + type + str(i) + " " +  "type" + " " + type)
   for n in range(0,toggles):
      nexthopgroup_list.append("size 100")
      #time.sleep(1)
      nexthopgroup_list.append("no size")   
capiCmd(switch,nexthopgroup_list)


