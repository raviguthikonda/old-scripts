# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
ospfadv = ['enable','configure','router ospf 1']
for i in range(0,16,2):
   ospfadv.append("network 20.0.0." + str(i) + "/31 area 0")
print ospfadv
capiCmd(switch,ospfadv)

