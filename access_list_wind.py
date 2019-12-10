# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from arstCliLib import capiCmd

#pbr configuration

switch = sys.argv[1]
no_of_entries = int(sys.argv[2])
acl_list = ['enable','configure','ip access-list acl-pbr1','statistics per-entry']
i = 2
j = 0
for k in range(no_of_entries):
   if i > 255:
      j = j+1
      i = 0
   cmd2 = "permit ip 104.1.%s.%s/32 101.1.%s.%s/32" %(j,i,j,i)
   acl_list.append(cmd2)
   i = i + 1
print acl_list
capiCmd(switch,acl_list)
