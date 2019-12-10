# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

switch = sys.argv[1]
sh_list = ['enable']
i = 0
nhgs = int(sys.argv[2])
for i in range(0,nhgs):
   tunsrc = '|' +  "1.1.1." + str(i)
   tunsrcip = ' \'' +  tunsrc + ' \' '
#   print tunsrcip
   sh_plat = "show platform arad ip nexthop-group | grep " + tunsrcip + " " +  "| wc -l"
   sh_list.append(sh_plat)
sh = capiCmd(switch,sh_list,capiFormat='text')
print sh
