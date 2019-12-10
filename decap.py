# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd
switch = sys.argv[1]
dcgs = int(sys.argv[2])  #no of decap groups
decapgroup_list = ['enable','configure']
type = sys.argv[3]
i = 0;j = 0
for n in range(0,dcgs):
   decapgroup_list.append("ip decap-group " + type + str(n))
   decapgroup_list.append("tunnel type " + type)
   if type == 'ipip':
      decapgroup_list.append("tunnel decap-interface vlan " + str(1501+i))
   elif type == 'gre':
      if i > 255:
         i = 0
         j = j+1
      ip = "150.%s.%s.15" %(j,i)
      decapgroup_list.append("tunnel decap-ip" + " " + ip)
   i = i+1
print decapgroup_list
capiCmd(switch,decapgroup_list)

