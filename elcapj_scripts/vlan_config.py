# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
interface_list = ['enable','configure']
for i in range (1,36,2):
   interface = "interface ethernet" + " 9/" + str(i) + "/1" + ",9/" +str(i+1) + "/1"
   interface_list.append(interface)
   interface_list.append("switchport mode access")
   switchport = "switchport access vlan " +str(i+101)
   interface_list.append(switchport)
   interface_list.append("vlan " + str(i+101))
print interface_list
capiCmd(switch,interface_list)
