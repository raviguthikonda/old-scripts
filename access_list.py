# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

#pbr configuration

switch = sys.argv[1]
no_of_entries = int(sys.argv[2])
acl_list = ['enable','configure','ip access-list acl-3k-rp-egress','statistics per-entry']
i = 0
j = 0
for k in range(no_of_entries):
   if i > 255:
      j = j+1
      i = 0
   cmd2 = "deny ip any 104.%s.%s.1/24" %(j,i)
   acl_list.append(cmd2)
   i = i + 1

capiCmd(switch,acl_list)
