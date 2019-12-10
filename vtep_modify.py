# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
max_vtep = int(sys.argv[2])
n = 0
flood_list_add = ['enable','configure','interface vxlan 1']
flood_list_remove = ['enable','configure','interface vxlan 1']
vtep_add = 'vxlan flood vtep add'
vtep_remove = 'vxlan flood vtep remove'
for i in range(0,50):
  for j in range(0,256):
    if n==max_vtep:
      break
    vtep_add += (' 9.0.%d.%d' %(i,j))
    vtep_remove += (' 9.0.%d.%d' %(i,j))
    #vtep =+ 'vxlan flood vtep add 9.0.%d.%d' %(i,j)
    #flood_list.append(vtep)
    #print(n)
    n = n+1
flood_list_add.append(vtep_add)
flood_list_remove.append(vtep_remove)
print flood_list_add
print flood_list_remove
time = int(sys.argv[3])
for t in range(0,time):
   capiCmd(switch,flood_list_add)
   capiCmd(switch,flood_list_remove)
   capiCmd(switch,flood_list_add)
