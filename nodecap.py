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
   decapgroup_list.append("no ip decap-group " + type + str(n))
print decapgroup_list
capiCmd(switch,decapgroup_list)

