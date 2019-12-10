# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
import sys
import time
from arstCliLib import capiCmd
switch = sys.argv[1]
svi_list = ['enable','configure']
j = 0
k = 0
for i in range(2, 4002):
   svi = 'interface vlan %d' % (i)
   svi_list.append(svi)
   if j > 255:
      j = 0
      k = k + 1
   svi_ip = 'ip address virtual 20.%d.%d.4/24' % (k, j)
   svi_list.append(svi_ip)
   j = j + 1
print svi_list
capiCmd(switch,svi_list)

