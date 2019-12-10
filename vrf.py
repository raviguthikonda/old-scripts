# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from arstCliLib import capiCmd

#pbr configuration

switch = sys.argv[1]
no_of_vrfs = int(sys.argv[2])
vrf_list = ['enable','configure']
port_channel_list = ['enable','configure']
routing_enable = ['enable','configure']
i = 1
j = 0
for k in range(289,no_of_vrfs,2):
   vrf_name = 'vrf definition vrf-' + str(k) 
   print vrf_name
   vrf_list.append(vrf_name)
print vrf_list
for k in range(289,no_of_vrfs,2):
   port_channel_config = 'interface port-Channel ' +str(k+1) + ','+str(k+2)
   ipv4_route_enable = 'ip routing vrf vrf-' +str(k)
   ipv6_route_enable = 'ipv6 unicast-routing vrf vrf-' +str(k)
   routing_enable.append(ipv4_route_enable)
   routing_enable.append(ipv6_route_enable)
   vrf_allocation = 'vrf forwarding vrf-' +str(k)
   port_channel_list.append(port_channel_config)
   port_channel_list.append(vrf_allocation)
print port_channel_list
print routing_enable
   
capiCmd(switch,vrf_list)
capiCmd(switch,port_channel_list)
capiCmd(switch,routing_enable)
