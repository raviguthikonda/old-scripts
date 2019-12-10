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
bgp_vrf = ['enable','configure','router bgp 65511']
i = 1
j = 0
f = open('/home/ravi.guthikonda/tmp/bgp.txt','r')
a = f.read()
#print a
l = a.split('\n')
l.pop()
#print l
print len(l)
j = 0
k = 1
for i in range(3,(len(l)),2):
   router_bgp_vrf = 'vrf vrf-' +str(i)
   bgp_vrf.append(router_bgp_vrf)
   bgp_vrf.extend([l[j],l[k]])
   j = j+2
   k = k+2
print bgp_vrf
#capiCmd(switch,bgp_vrf)   

















   



