# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

switch = sys.argv[1]
sh_list = ['enable','show platform trident l3 shadow next-hops multipath']
sh = capiCmd(switch,sh_list,capiFormat='text')
i = 0
for each in sh:
   if 'Multipath Egress Object' in  each['output']:
      split_list = each['output'].split('Multipath Egress Object')
      for each in split_list:
         if 'Interfaces' in each:
            wo_interfaces = each.replace('Interfaces: ','')  #Deleted interfaces word from the string
            nh_group_entries = wo_interfaces.split()
            nh_group_id = nh_group_entries.pop(0)
            print 'no of entries in nexthop group ' + nh_group_id + " is " + str( (len(nh_group_entries)))
            print "======================================"
