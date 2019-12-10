# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.


import sys
from cliLib import capiCmd
switch = sys.argv[1]
cmd1 = "set nexthop 11.0.0.1"
ospf_adv = ["enable","configure","router ospf 1","network 11.0.0.0/31 area 0"]
for i in range(3,256,2):
   cmd1 = cmd1 + " "
   #inc = 50 + i
   nh = "11.0.0." + str(i)
   network = "network 11.0.0." + str(i-1) + "/31 area 0"
   ospf_adv.append(network)
   cmd1 = cmd1 + nh

print cmd1
print ospf_adv
capiCmd(switch,ospf_adv)
