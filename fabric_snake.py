# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

from arstCliLib import capiCmd
import sys
switch=sys.argv[1]
n = 2
interface_list = []
for i in range(1,37):
  interface_list.append('Ethernet'+ '8/'+ str(i) +'/1')
#print(interface_list)
interface_list1 = interface_list[0:18]
interface_list2 = interface_list[18:36]
#print(interface_list1)
#print(interface_list2)
fabric_snake_config = ['enable','configure']
n = len(interface_list1)
for i in range(0,n):
  fabric_snake_config.append('interface' + ' ' + interface_list1[i] + ',' + interface_list2[n-2] )
  fabric_snake_config.append('switchport access vlan %d'% (i+2))
  n = n-1
print(fabric_snake_config)
#capiCmd(switch,fabric_snake_config)
