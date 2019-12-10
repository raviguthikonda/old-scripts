# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

switch = sys.argv[1]
vlan_list = ["enable","configure"]
for n in range(1501,1511):
   svi = "interface vlan " + str(n)
   vlan_list.append(svi)
   #if n < 561 or n > 1040:
   for i in range(1,11):
      vlan_list.append("no service-policy type pbr input pbr-" + str(n))
      vlan_list.append("service-policy type pbr input pbr-" + str(n))
#prin vlan_list
#capiCmd(switch,ospf_adv)
print vlan_list
capiCmd(switch,vlan_list)
#capiCmd(switch,policy_list)
#capiCmd(switch,ping_list)
#capiCmd(switch,neighbor_list)
