# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

i = 0
j = 0
switch = sys.argv[1]
vlan_list = ["enable","configure","vlan 1501-2524"]
ospf_adv = ["enable","configure","router ospf 1"]
policy_list = ["enable","configure"]
ping_list = ["enable","configure"]
for n in range(1500,2012):
   #if n < 561 or n > 1040:
   svi = "interface vlan " + str(n)
   vlan_list.append(svi)
   #vlan_list.append("service-policy type pbr input pbr-" + str(n))
   if i > 255:
      i = 0
      j = j+1
   ip_address = "ip address 150." + str(j) + "." + str(i) + "." + "15/24"
   next_hop = "150." + str(j) + "." + str(i) + ".5"
   #next_hop2 = "150." + str(j) + "." + str(i) + ".10"
   #ping_ip = "150." + str(j) + "." + str(i) + ".1"
   #ping_list.append("ping" + " " + ping_ip)
   network = "network 150." + str(j) + "." + str(i) + "." + "0/24 area 0"
   policy_list.append("policy-map type pbr pbr-" + str(n))
   match_ip = "150." + str(j) + "." + str(i) + ".1/24"
   #policy_list.append("10 match ip " + match_ip + " any" + " set nexthop " + next_hop)
   policy_list.append("10 match ip " + match_ip + " any" + " set nexthop " + next_hop)
   #policy_list.append("10 match ip " + match_ip + " any" + " set nexthop 150.0.0.5 150.0.1.5 150.0.2.5 150.0.3.5 150.0.4.5 150.0.5.5 150.0.6.5 150.0.7.5 150.0.8.5 150.0.9.5 150.0.10.5 150.0.11.5 150.0.12.5 150.0.13.5 150.0.14.5 150.0.15.5 150.0.16.5 150.0.17.5 150.0.18.5 150.0.19.5 150.0.20.5 150.0.21.5 150.0.22.5 150.0.23.5 150.0.24.5 150.0.25.5 150.0.26.5 150.0.27.5 150.0.28.5 150.0.29.5 150.0.30.5 150.0.31.5 150.0.32.5 150.0.33.5 150.0.34.5 150.0.35.5 150.0.36.5 150.0.37.5 150.0.38.5 150.0.39.5 150.0.40.5 150.0.41.5 150.0.42.5 150.0.43.5 150.0.44.5 150.0.45.5 150.0.46.5 150.0.47.5 150.0.48.5 150.0.49.5 150.0.50.5 150.0.51.5 150.0.52.5 150.0.53.5 150.0.54.5 150.0.55.5 150.0.56.5 150.0.57.5 150.0.58.5 150.0.59.5 150.0.60.5 150.0.61.5 150.0.62.5 150.0.63.5 150.0.64.5 150.0.65.5 150.0.66.5 150.0.67.5 150.0.68.5 150.0.69.5 150.0.70.5 150.0.71.5 150.0.72.5 150.0.73.5 150.0.74.5 150.0.75.5 150.0.76.5 150.0.77.5 150.0.78.5 150.0.79.5 150.0.80.5 150.0.81.5 150.0.82.5 150.0.83.5 150.0.84.5 150.0.85.5 150.0.86.5 150.0.87.5 150.0.88.5 150.0.89.5 150.0.90.5 150.0.91.5 150.0.92.5 150.0.93.5 150.0.94.5 150.0.95.5 150.0.96.5 150.0.97.5 150.0.98.5 150.0.99.5 150.0.100.5 150.0.101.5 150.0.102.5 150.0.103.5 150.0.104.5 150.0.105.5 150.0.106.5 150.0.107.5 150.0.108.5 150.0.109.5 150.0.110.5 150.0.111.5 150.0.112.5 150.0.113.5 150.0.114.5 150.0.115.5 150.0.116.5 150.0.117.5 150.0.118.5 150.0.119.5 150.0.120.5 150.0.121.5 150.0.122.5 150.0.123.5 150.0.124.5 150.0.125.5 150.0.126.5 150.0.127.5")
   ospf_adv.append(network)
   #neighbor_list.append(neighbor)
   vlan_list.append(ip_address)
   i = i+1
#prin vlan_list
capiCmd(switch,ospf_adv)
print vlan_list
capiCmd(switch,vlan_list)
#capiCmd(switch,policy_list)
#capiCmd(switch,ping_list)
#capiCmd(switch,neighbor_list)
