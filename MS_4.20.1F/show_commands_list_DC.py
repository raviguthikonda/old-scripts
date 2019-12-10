# Copyright (c) 2019 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from arstCliLib import capiCmd
switches = sys.argv[2:]
platform = sys.argv[1]
print platform
show_commands_list = []
if 'sand' in platform:
   show_commands_list = ['show bfd neighbors vrf all'          
,'show ip bgp detail vrf all'   
,'show ip mroute vrf default count'  
,'show ip pim vrf default neighbor'  
,'show ip route vrf all'              
,'show vrrp all'
,'show bfd neighbors vrf all detail'   
,'show ip bgp summary vrf all'  
,'show ip ospf database vrf all'     
,'show ip rip database vrf all'      
,'show ip route vrf default summary'  
,'show vrrp vrf all brief all'
,'show interfaces counters rates | nz'  
,'show ip mroute vrf default'   
,'show ip ospf neighbor vrf all'     
,'show ip rip neighbors vrf all'
,'show platform fap ip route summary'
,'show platform sand l3 summary']
elif 'strata' in platform:
   print 1
   show_commands_list = ['show bfd neighbors vrf all'
            ,'show ip bgp detail vrf all'
            ,'show ip mroute vrf default count'
            ,'show ip pim vrf default neighbor'
            ,'show ip route vrf all'
            ,'show vrrp all'
            ,'show bfd neighbors vrf all detail'
            ,'show ip bgp summary vrf all'
            ,'show ip ospf database vrf all'
            ,'show ip rip database vrf all'
            ,'show ip route vrf default summary'
            ,'show vrrp vrf all brief all'
            ,'show interfaces counters rates | nz'
            ,'show ip mroute vrf default'
            ,'show ip ospf neighbor vrf all'
            ,'show ip rip neighbors vrf all'
            ,'show platform trident l3 summary']
show_commands_list1 = []
for each_command in show_commands_list:
   each_command1 = each_command.replace(' ','_')
   each_command2 = each_command1.replace('|','_')
   show_commands_list1.append(each_command2)
for switch in switches:
   send_command = ['enable','configure','mkdir' + ' '  + switch]
   for i in range(len(show_commands_list)):
      if '|' in show_commands_list[i]:
         print 'ifloop'
         command = show_commands_list[i] + ' > ' + '/mnt/flash/' + switch + '/' + show_commands_list1[i]
         send_command.append(command)
      else:
         print 'elseloop'
         command = show_commands_list[i] + ' > ' + 'flash:' + switch + '/' + show_commands_list1[i]
         print command
         send_command.append(command)
   print send_command
   capiCmd(switch,send_command,capiFormat='text')

