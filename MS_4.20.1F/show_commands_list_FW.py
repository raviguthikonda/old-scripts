# Copyright (c) 2019 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from arstCliLib import capiCmd
switches = sys.argv[1:]
show_commands_list = ['show bfd neighbors vrf all'          
      ,'show ip ospf neighbor vrf all'           
      ,'show ip route vrf AssetClass-4 summary'      
      ,'show ip route vrf SecureEnclave-5 summary'  
      ,'show ip route vrf default summary'
      ,'show bfd neighbors vrf all detail'   
      ,'show ip rip database vrf all'            
      ,'show ip route vrf SecureEnclave-10 summary'  
      ,'show ip route vrf SecureEnclave-6 summary'  
      ,'show platform trident l3 summary'
      ,'show interfaces counters rates | nz'  
      ,'show ip rip neighbors vrf all'           
      ,'show ip route vrf SecureEnclave-1 summary'   
      ,'show ip route vrf SecureEnclave-7 summary'  
      ,'show vrrp all'
      ,'show ip bgp detail vrf all'          
      ,'show ip route vrf AssetClass-1 summary'  
      ,'show ip route vrf SecureEnclave-2 summary'   
      ,'show ip route vrf SecureEnclave-8 summary'  
      ,'show vrrp vrf all brief all'
      ,'show ip bgp summary vrf all'         
      ,'show ip route vrf AssetClass-2 summary'  
      ,'show ip route vrf SecureEnclave-3 summary'   
      ,'show ip route vrf SecureEnclave-9 summary'
      ,'show ip ospf database vrf all'       
      ,'show ip route vrf AssetClass-3 summary'  
      ,'show ip route vrf SecureEnclave-4 summary'   
      ,'show ip route vrf all']          
show_commands_list1 = []
for each_command in show_commands_list:
   each_command1 = each_command.replace(' ','_')
   each_command2 = each_command1.replace('|','_')
   show_commands_list1.append(each_command2)
for switch in switches:
   send_command = ['enable','configure','mkdir' + ' '  + switch]
   for i in range(len(show_commands_list)):
      if '|' in show_commands_list[i]:
         command = show_commands_list[i] + ' > ' + '/mnt/flash/' + switch + '/' + show_commands_list1[i]
         send_command.append(command)
      else:
         command = show_commands_list[i] + ' > ' + 'flash:' + switch + '/' + show_commands_list1[i]
         send_command.append(command)
   print send_command
   capiCmd(switch,send_command,capiFormat='text')

