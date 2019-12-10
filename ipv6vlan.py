# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

i = 0
j = 0
switch = sys.argv[1]
vlan_list = ["enable","configure","vlan 1500-2011"]
for n in range(1500,2011):
   #if n < 561 or n > 1040:
   svi = "interface vlan " + str(n)
   vlan_list.append(svi)
   #vlan_list.append("service-policy type pbr input pbr-" + str(n))
   ipv6_address = "ipv6 address " + str(n) + "::" + str(15) + "/64"
   #network = "network 150." + str(j) + "." + str(i) + "." + "0/24 area 0"
   vlan_list.append(ipv6_address)
   i = i+1
#prin vlan_list
#capiCmd(switch,ospf_adv)
print vlan_list
capiCmd(switch,vlan_list)
#capiCmd(switch,policy_list)
#capiCmd(switch,ping_list)
#capiCmd(switch,neighbor_list)
