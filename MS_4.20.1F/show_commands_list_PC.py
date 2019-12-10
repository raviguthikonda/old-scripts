# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
# this script is for show commands on wa403,wps105,wa456,yo407
import sys
from arstCliLib import capiCmd
switches = sys.argv[1:]
show_commands_list = ['show bfd neighbors vrf all'             
      ,'show ip mroute vrf AssetClass-4'         
      ,'show ip msdp vrf AssetClass-4 summary'   
      ,'show ip route vrf AssetClass-2 summary'      
      ,'show ip route vrf SecureEnclave-8 summary'
      ,'show bfd neighbors vrf all detail'      
      ,'show ip mroute vrf AssetClass-4 count'   
      ,'show ip ospf database vrf all'           
      ,'show ip route vrf AssetClass-3 summary'      
      ,'show ip route vrf SecureEnclave-9 summary'
      ,'show interfaces counters rates | nz'
      ,'show ip mroute vrf default'              
      ,'show ip ospf neighbor vrf all'           
      ,'show ip route vrf AssetClass-4 summary'      
      ,'show ip route vrf all'
      ,'show ip bgp detail vrf all'             
      ,'show ip mroute vrf default count'        
      ,'show ip pim vrf AssetClass-1 neighbor'   
      ,'show ip route vrf SecureEnclave-10 summary'  
      ,'show ip route vrf default summary'
      ,'show ip bgp summary vrf all'            
      ,'show ip msdp vrf AssetClass-1 sa-cache'  
      ,'show ip pim vrf AssetClass-2 neighbor'   
      ,'show ip route vrf SecureEnclave-1 summary'   
      ,'show platform fap ip route summary'
      ,'show ip mroute vrf AssetClass-1'        
      ,'show ip msdp vrf AssetClass-1 summary'   
      ,'show ip pim vrf AssetClass-3 neighbor'   
      ,'show ip route vrf SecureEnclave-2 summary'   
      ,'show platform sand l3 summary'
      ,'show ip mroute vrf AssetClass-1 count'  
      ,'show ip msdp vrf AssetClass-2 sa-cache'  
      ,'show ip pim vrf AssetClass-4 neighbor'   
      ,'show ip route vrf SecureEnclave-3 summary'   
      ,'show vrrp all'
      ,'show ip mroute vrf AssetClass-2'        
      ,'show ip msdp vrf AssetClass-2 summary'   
      ,'show ip pim vrf default neighbor'        
      ,'show ip route vrf SecureEnclave-4 summary'   
      ,'show vrrp vrf all brief all'
      ,'show ip mroute vrf AssetClass-2 count'  
      ,'show ip msdp vrf AssetClass-3 sa-cache'  
      ,'show ip rip database vrf all'            
      ,'show ip route vrf SecureEnclave-5 summary'
      ,'show ip mroute vrf AssetClass-3'        
      ,'show ip msdp vrf AssetClass-3 summary'   
      ,'show ip rip neighbors vrf all'           
      ,'show ip route vrf SecureEnclave-6 summary'
      ,'show ip mroute vrf AssetClass-3 count'  
,'show ip msdp vrf AssetClass-4 sa-cache'  
,'show ip route vrf AssetClass-1 summary'  
,'show ip route vrf SecureEnclave-7 summary']
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

