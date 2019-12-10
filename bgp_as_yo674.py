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
bgp_vrf = ['enable','configure','router bgp 65513']
i = 1
j = 0
f = open('/home/ravi.guthikonda/tmp/bgp_v6_yo674_as.txt','r')
a = f.read()
#print a
l = a.split('\n')
l.pop()
#print l
print len(l)
j = 0
k = 1
p = 2
q = 3
as_no = 6
neighbor_as_list = []
remote_as_list = []
neighbor_activate_list = []
for m in range(2,len(l)):
   neighbor = l[m]
   n = neighbor.split('peer-group')
   #print n
   neighbor_as = n[0] + ' ' + 'local-as' + ' ' + str(as_no) + ' ' +  'no-prepend replace-as'
   remote_as_peer = n[0] + 'remote-as' + ' ' + str(as_no-1)
   #print neighbor_as
   neighbor_as_list.append(neighbor_as)
   neighbor_as_list.append(remote_as_peer)
   neighbor_activate = n[0] + ' ' + 'activate'
   neighbor_activate_list.append(neighbor_activate)
   as_no = as_no + 2
#print neighbor_as_list
vrf_no = 3
r = 0
s = 1
#print len(neighbor_as_list)
for i in range(0,(len(neighbor_as_list)),4):
   router_bgp_vrf = 'vrf vrf-' +str(vrf_no)
   vrf_no = vrf_no + 2
   #print vrf_no
   if i >= 568:
      break
   else:
      bgp_vrf.append(router_bgp_vrf)
      bgp_vrf.extend([neighbor_as_list[j],neighbor_as_list[k],neighbor_as_list[p],neighbor_as_list[q]])
      bgp_vrf.append('address-family ipv6')
      bgp_vrf.extend([neighbor_activate_list[r],neighbor_activate_list[s]])
   #print neighbor_as_list[j]
   #print neighbor_as_list[k]
   #print neighbor_as_list[p]
   #print neighbor_as_list[q]



      j = j+4
      k = k+4
      p = p+4
      q = q+4
      r = r+2
      s = s+2
print bgp_vrf
capiCmd(switch,bgp_vrf)   

















   



