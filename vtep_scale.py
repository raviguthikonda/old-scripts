# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
#from cliLib import capiCmd
switch = sys.argv[1]
max_vtep = int(sys.argv[2])
n = 0
flood_list = ['enable','configure','interface vxlan 1']
vtep = 'vxlan flood vtep add'
for i in range(0,255):
  for j in range(1,256):
    if n==max_vtep:
      break
    vtep += (' 8.0.%d.%d' %(i,j))
    #vtep =+ 'vxlan flood vtep add 9.0.%d.%d' %(i,j)
    #flood_list.append(vtep)
    #print(n)
    n = n+1
flood_list.append(vtep)
print flood_list
#capiCmd(switch,flood_list)
